class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = [0]
        
        self.dfs(rooms, 0)
        #print(self.visited)
        if len(self.visited) == len(rooms):
            return True
        return False
        
    def dfs(self, rooms, i):
        keys = rooms[i]
        
        for key in keys:
            if key not in self.visited:
                self.visited.append(key)
                self.dfs(rooms, key)
                
            else:
                continue
        return

