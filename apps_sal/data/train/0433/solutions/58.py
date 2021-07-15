class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c = 0
        s = sum(arr[:k])
        if s/k >=threshold :
                c=1
        i = 1
        while i<= len(arr) - k:
            s = s - arr[i-1] + arr[i+k-1]
            if s/k >=threshold :
                c+=1
            i+=1
        return c
