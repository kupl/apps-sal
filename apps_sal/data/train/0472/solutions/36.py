class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen=set()
        return self.dfs(arr,start,seen)
    
    def dfs(self,arr,idx,seen):
        if idx>=len(arr) or (idx<0) or (idx in seen):
            return False
        if arr[idx]==0:
            return True
        seen.add(idx)
        return self.dfs(arr,idx-arr[idx],seen) or self.dfs(arr,idx+arr[idx],seen)
