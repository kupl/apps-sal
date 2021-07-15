class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A or len(A) < 3:
            return 0
        
        left = right = mid = max_moun = 0
        while right < len(A):
            
            prev = mid
            while right + 1 < len(A) and A[right + 1] > A[right]:
                right += 1
                mid += 1
                
            if prev != mid:
                while right + 1 < len(A) and A[right + 1] < A[right]:
                    right += 1

                if mid != 0 and mid != len(A) - 1:
                    max_moun = max(max_moun, right - left + 1)
            
            right = mid + 1
            left = right
            mid = right
            
        if max_moun < 3:
            return 0
        
        return max_moun
