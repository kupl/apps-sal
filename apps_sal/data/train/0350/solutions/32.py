from collections import Counter


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.at_most(A, K) - self.at_most(A, K - 1)

    def at_most(self, a, k):
        res = 0
        start = 0
        c = Counter()
        for (end, elem) in enumerate(a):
            if c[elem] == 0:
                k -= 1
            c[elem] += 1
            while start <= end and k < 0:
                c[a[start]] -= 1
                if c[a[start]] == 0:
                    k += 1
                start += 1
            res += end - start + 1
        return res
