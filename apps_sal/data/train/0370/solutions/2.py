#
# @lc app=leetcode id=952 lang=python3
#
# [952] Largest Component Size by Common Factor
#

# @lc code=start
from collections import defaultdict


class Solution:
    MAXPRIME = 100001
    isPrime = [0 for _ in range(MAXPRIME + 1)]
    isPrime[0] = -1
    isPrime[1] = -1  # 0 and 1 are not prime numbers
    for i in range(2, MAXPRIME):
        if isPrime[i] == 0:  # i is prime
            for multiple in range(i * i, MAXPRIME + 1, i):
                if isPrime[multiple] == 0:
                    isPrime[multiple] = i
            isPrime[i] = i

    def largestComponentSize(self, A: List[int]) -> int:
        label = defaultdict(int)

        def findRoot(key):
            if label[key] > 0:
                label[key] = findRoot(label[key])
                return label[key]
            else:
                return key

        def mergeRoot(k1, k2):
            r1, r2 = findRoot(k1), findRoot(k2)
            if r1 != r2:
                r1, r2 = min(r1, r2), max(r1, r2)
                label[r1] += label[r2]
                label[r2] = r1
            return r1

        for x in A:
            root_id = 0
            prime_factors = set()
            while Solution.isPrime[x] != -1:
                p = Solution.isPrime[x]
                root_id = findRoot(p) if root_id == 0 else mergeRoot(root_id, p)
                x //= p
            label[root_id] -= 1

        return -min(label.values())
# @lc code=end
