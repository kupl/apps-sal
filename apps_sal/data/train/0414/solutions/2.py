class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        check=arr[0]
        count=0
        for i in range(1,len(arr)):
            if check>arr[i]:
                count+=1
            else:
                check=arr[i]
                count=1
            if count==k:
                return check
        return check
                
        

