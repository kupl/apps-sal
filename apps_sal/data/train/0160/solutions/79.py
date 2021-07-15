class Solution:
    def __init__(self):
        self.result=False
    
    def backtrack(self,arr,start,end,alex,lee,count,visited):
        if start>end and lee<alex:
              return 1
        elif start>end:
            return 0
        elif visited[start][end]!=-1:
            return visited[start][end]
        else:
            a,b=0,0
            if count%2==0:                a=max(self.backtrack(arr,start+1,end,alex+arr[start],lee,count+1,visited),self.backtrack(arr,start,end-1,alex+arr[end],lee,count+1,visited))
            else:                b=max(self.backtrack(arr,start+1,end,alex,lee+arr[start],count+1,visited),self.backtrack(arr,start,end-1,alex,lee+arr[end],count+1,visited))
            visited[start][end]=max(visited[start][end],a,b)
            return visited[start][end]    
                
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        visited=[-1 for i in range(n)]
        for i in range(n):
            visited[i]=[-1 for i in range(n)]
        
        if self.backtrack(piles,0,len(piles)-1,0,0,0,visited):
            return True
        return False
        
        
        

