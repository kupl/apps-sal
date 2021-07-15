class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        cache = {}
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                # print(cache)
                diff = A[j] - A[i]
                if (i, diff) in cache:
                    cache[j, diff] = cache[i, diff] + 1
                    ans = max(cache[j, diff], ans)
                else:
                    cache[j, diff] = 2
                    ans = max(cache[j, diff], ans)
        return ans


