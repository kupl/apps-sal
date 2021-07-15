from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        def atMostK(nums, k):
            print(nums, k)
            res, left = 0, 0
            counter = Counter()
            for right, v in enumerate(nums):
                if counter[v] == 0:
                    k -= 1
                counter[v] += 1
                while k < 0:
                    counter[A[left]] -= 1
                    if counter[A[left]] == 0:
                        k += 1
                    left += 1
                res += right - left
                # print(counter, res)
            return res
        return atMostK(A, K) - atMostK(A, K-1)
