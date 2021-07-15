class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        longestMountain = 0

        for i in range(1, len(A) - 1):
            # Index i denotes a 'peak' in the mountain.
            if A[i - 1] < A[i] > A[i + 1]:
                left = right = i
                
                # Traverse left and down the mountain from i until there is no longer a downwards slope.
                while left > 0 and A[left - 1] < A[left]:
                    left -= 1
                                
                # Traverse right and down the mountain from i until there is no longer a downwards slope.
                while right + 1 < len(A) and A[right + 1] < A[right]:
                    right += 1
                    
                # The length of the mountain will be the distance from left and right (+ 1 to factor in the peak).
                mountainLength = right - left + 1
                longestMountain = max(longestMountain, mountainLength)
        
        return longestMountain
