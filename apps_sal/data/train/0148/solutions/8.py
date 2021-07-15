class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr=[0 for _ in range(10**5+1)]
        for i in range(len(profit)):
            arr[difficulty[i]]=max(profit[i],arr[difficulty[i]])
        for i in range(1,10**5+1):
            arr[i]=max(arr[i-1],arr[i])
        ans=0
        # print(arr[:101])
        for i in worker:
            ans+=arr[i]
        return ans

