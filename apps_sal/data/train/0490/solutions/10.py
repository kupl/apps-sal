class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        q=deque([])
        vis=[False]*len(rooms)
        q.append(0)
        
        while q:
            ver=q.popleft()
            vis[ver]=True
            for neigh in rooms[ver]:
                if(vis[neigh]!=True):
                    q.append(neigh)

        if(False in vis):
            return False
        else:
            return True
          
            
        

