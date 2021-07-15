class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        increasing = False
        count = -float('inf')
        last = A[0]
        max_len = 0
        for i in range(1,len(A)):
            if A[i] > last and increasing:
                count += 1
            elif A[i] > last and not increasing:
                count = 2
                increasing = True
            elif A[i] < last and increasing:
                count += 1
                increasing = False
                max_len = max(max_len, count)
            elif A[i] < last and not increasing:
                count += 1
                max_len = max(max_len, count)
            else:
                if not increasing:
                    max_len = max(max_len, count)
                count = -float('inf')
                increasing = False
            last = A[i]
        
        if max_len < 3:
            return 0
        return max_len
                



