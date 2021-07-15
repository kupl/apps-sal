class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        list_of_rooms_visited = [0]
        
        def check(arr):
            #print(list_of_rooms_visited)
            for j in arr:
                if j not in list_of_rooms_visited:
                    list_of_rooms_visited.append(j)
                    check(rooms[j])
            return
                
        check(rooms[0])
        if len(list_of_rooms_visited)!=len(rooms):
            return False
        else:
            return True

