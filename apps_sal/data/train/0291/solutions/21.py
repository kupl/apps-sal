class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans=0
        evenCount=0
        oddCount=0
        for i in arr:
            if(i%2==0):
                ans+=oddCount
                oddCount, evenCount = oddCount, evenCount+1
            else:
                ans+=evenCount+1
                oddCount, evenCount = evenCount+1, oddCount
        return int(ans%(math.pow(10,9)+7))
