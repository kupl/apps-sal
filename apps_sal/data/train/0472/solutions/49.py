class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        q=[start]
        while q:
            node=q.pop(0)
            #print(arr[node])
            if arr[node]==0:
                return True
            if arr[node]<0:
                continue
            for i in [node+arr[node],node-arr[node]]:
                #print(i)
                if i>=0 and i<n:
                    q.append(i)
            #print(q)
            arr[node]=-arr[node]
            #print(arr)
        return False
