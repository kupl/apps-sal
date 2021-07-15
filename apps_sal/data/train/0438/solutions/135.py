class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:           
        d = set([0,len(arr) + 1])
        if m == len(arr): return m
        for i in range(len(arr)-1,-1,-1):
            if arr[i] - m - 1 in d:
                exit = True
                for j in range(arr[i] - m , arr[i]):
                    if j in d:
                        exit = False
                        break
                if exit:
                    return i
            if arr[i] + m+1 in d:
                exit = True
                for j in range(arr[i]+1,arr[i]+m+1):
                    if j in d:
                        exit = False
                        break
                if exit:
                    return i
            d.add(arr[i])
        
        return -1
                

