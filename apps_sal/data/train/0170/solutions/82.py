class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        '''
        [1,2,3,10,4,2,3,5]
        3
        
        '''
        def doesExist(arr, size, prefix, suffix):
            if size >= suffix or (len(arr) -1 - size) <= prefix:
                return True
            for i in range(len(arr) - size - 1):
                if prefix < i:
                    break
                else:
                    j = i + size + 1
                    if arr[i] <= arr[j] and j >= suffix:
                        return True
            return False
          
        prefix = 0
        suffix = len(arr) - 1
        for i in range(1, len(arr)):
            if arr[i-1] <= arr[i]:
                prefix = i
            else:
                break
        
        for i in range(len(arr) - 1, 0, -1):
            if arr[i-1] <= arr[i]:
                suffix = i - 1
            else:
                break
                
        l = 0
        r = len(arr) - 1
        optimal = r
        while l <= r:
            mid = (l + r) // 2
            if doesExist(arr, mid, prefix, suffix):
                optimal = mid
                r = mid - 1
            else:
                l = mid + 1
        return optimal
        

