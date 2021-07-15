from collections import defaultdict
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        total = sum(A)
        size = len(A)
        possible = False
        for i in range(size//2):
            if total*i % size == 0:
                possible = True
                break
        if not possible:
            return False
        dp = defaultdict(set)
        dp[0].add(0)
        for n in A:
            for i in range(size//2, 0, -1):
                for ele in dp[i-1]:
                    dp[i].add(ele+n)
        for i in range(1, size//2+1):
            if total*i % size == 0 and total*i//size in dp[i]:
                return True
        return False
