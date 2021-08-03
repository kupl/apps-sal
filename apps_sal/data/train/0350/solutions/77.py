class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMost(k):
            counter = collections.defaultdict(int)
            i = res = 0
            for j, v in enumerate(A):
                counter[v] += 1
                while len(counter) > k:
                    counter[A[i]] -= 1
                    if counter[A[i]] == 0:
                        del counter[A[i]]
                    i += 1
                res += j - i + 1
            return res

        return atMost(K) - atMost(K - 1)
