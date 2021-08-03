class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def subarraysWithDictinctAtMost(A: List[int], K: int) -> int:
            left, right = 0, 0
            ans = 0
            counter = dict()
            while right < len(A):
                if A[right] not in counter:
                    counter[A[right]] = 0
                counter[A[right]] += 1
                while len(counter) > K:
                    counter[A[left]] -= 1
                    if counter[A[left]] == 0:
                        counter.pop(A[left])
                    left += 1

                ans += right - left + 1
                right += 1
            return ans
        return subarraysWithDictinctAtMost(A, K) - subarraysWithDictinctAtMost(A, K - 1)
