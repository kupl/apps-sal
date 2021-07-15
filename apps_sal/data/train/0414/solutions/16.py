class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if(k>=len(arr)):
            return max(arr)
        maxi=arr[0]
        stream=0
        if(k==1):
            return max(arr[0],arr[1])
        for i in range(1,len(arr)):
            if(arr[i]>maxi):
                stream=1
                maxi=arr[i]
            else:
                stream+=1
            if(stream>=k):
                return maxi
        return max(arr)
                
            

