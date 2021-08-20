class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        left = res = cur_sum = count = 0
        for right in range(len(A)):
            cur_sum += A[right]
            if A[right] == 1:
                count = 0
            while left <= right and cur_sum >= S:
                if cur_sum == S:
                    count += 1
                cur_sum -= A[left]
                left += 1
            res += count
        return res
