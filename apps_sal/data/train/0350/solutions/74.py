class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atMost(A, K):
            left = res = 0
            hash_map = {}

            for right in range(len(A)):
                hash_map[A[right]] = hash_map.get(A[right], 0) + 1

                while len(hash_map) > K:
                    hash_map[A[left]] -= 1
                    if hash_map[A[left]] == 0:
                        del hash_map[A[left]]
                    left += 1
                res += right - left + 1
            return res

        return atMost(A, K) - atMost(A, K - 1)
