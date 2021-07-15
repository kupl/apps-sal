class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=0
        c=0
        for i in range(k):
            s=s+arr[i]
        if(s/k>=threshold):
            c=c+1
        for i in range(k,len(arr)):
            s=s+arr[i]
            s=s-arr[i-k]
            if(s/k>=threshold):
                c=c+1
        return c
        
                

