class Solution:
    def longestOnes(self, arr: List[int], K: int) -> int:
        left = 0

        for right in range(len(arr)):
            K -= 1 - arr[right]
            if K < 0:
                K += 1 - arr[left]
                left += 1

        return right - left + 1
