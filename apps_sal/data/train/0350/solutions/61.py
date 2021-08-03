class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atmost(k):
            i = 0
            res = 0
            d = defaultdict(int)

            for j, a in enumerate(A):
                if d[a] == 0:
                    k -= 1
                d[a] += 1
                while k < 0:
                    d[A[i]] -= 1
                    if d[A[i]] == 0:
                        k += 1
                    i += 1
                res += j - i + 1

            return res

        return atmost(K) - atmost(K - 1)
