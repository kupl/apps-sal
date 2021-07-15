class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr=[0]+arr
        res=0
        for k in range(1,len(arr)):
            arr[k]^=arr[k-1]
            for j in range(1,k+1):
                for i in range(1,j):
                    b=arr[k]^arr[j-1]
                    a=arr[j-1]^arr[i-1]
                    if a==b:
                        #print(i-1,j-1,k-1)
                        res+=1
        #print(arr)
        return res
