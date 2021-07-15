class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
                
        i=0; j=1; m=k
        while True:
            while j<len(arr) and arr[j]<arr[i]:
                m-=1; j+=1
            if m<=0 or j>=len(arr): return arr[i]
            i+=1; j=i+1; m=k-1

            

