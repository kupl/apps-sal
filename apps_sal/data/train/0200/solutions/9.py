class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        count=0
        while(k>=0):
            arr=[]
            arr.append(1)
            arr.append(1)
            while(arr[-1]+arr[-2]<=k):
                arr.append(arr[-1]+arr[-2])
            
            k-=arr[-1]
            count+=1
            
        return count-1
