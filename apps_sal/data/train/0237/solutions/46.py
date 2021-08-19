class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count = 0
        output = 0
        left = 0
        for right in range(len(A)):
            S -= A[right]
            if A[right] == 1:
                count = 0
            while left <= right and S <= 0:
                if S == 0:
                    count += 1
                S += A[left]
                left += 1
            output += count
        return output
