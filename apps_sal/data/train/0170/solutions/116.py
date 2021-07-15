class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        inc_idx = 0
        for i in range(1, len(arr)):
            if arr[i] >= arr[i-1]:
                inc_idx += 1
            else:
                break
    
        if inc_idx == len(arr) - 1:
            return 0
        
        dec_idx = len(arr) - 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] <= arr[i+1]:
                dec_idx -= 1
            else:
                break
        
        l = self.helper(arr[:inc_idx+1], arr[dec_idx:])
        return len(arr) - l
        
        
    def helper(self, arr1: List[int], arr2: List[int]):
        print((arr1, arr2))
        i, j = 0, 0
        l = 0
        while i < len(arr1) and j < len(arr2):
            while j < len(arr2) and arr1[i] > arr2[j]:
                j += 1
            if j == len(arr2):
                break
            
            l = max(l, i + 1 + len(arr2) - j)
            print((i, j, l))
            i += 1

        return max(len(arr1), len(arr2), l)
        

