from functools import lru_cache

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        '''
        1 2 3 10 4 2 3 5
            i
                     j
                       
        1  2 3
          ij
        '''
        N = len(arr)
        i = 0
        while i < N-1 and arr[i+1] >= arr[i]:
            i += 1
        left = N - i - 1
        
        j = N-1
        while j > 0 and arr[j-1] <= arr[j]:
            j -= 1
        right = j
        
        ret = N-1
        
        @lru_cache(maxsize=None)
        def search(i, j):
            print(i, j)
            nonlocal ret
            if i == j: return 0

            if arr[j] >= arr[i]:
                ret = min(ret, j-i-1)
            
            I = i
            while i < N-1 and arr[i+1] >= arr[i] and arr[i+1] <= arr[j]:
                i += 1
            if i > I:
                search(i, j)
            
            i = I
            J = j
            while j > 0 and arr[j-1] <= arr[j] and arr[j-1] >= arr[i]:
                j -= 1
            if j < J:
                search(i, j)
                    
        search(0, N-1)
        
        return min(left, ret, right)
