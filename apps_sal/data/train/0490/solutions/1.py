from collections import deque 

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False for i in range(len(rooms))]
        seen[0] = True 
        stack = deque()
        stack.append(0)
        
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not seen[key]:
                    seen[key] = True 
                    stack.append(key)
        
        return all(seen)

                
                
        

