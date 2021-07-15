import numpy as np
class Solution(object):
    def canVisitAllRooms(self, rooms):
        seenRooms = np.zeros(len(rooms), dtype = bool)
        Keys = [0]
        while(len(Keys)!=0):
            curr = Keys.pop(0)
            seenRooms[curr] = True
            for key in rooms[curr]:
                if not seenRooms[key]:
                    Keys.append(key)
        return True if all(seenRooms) else False
                
            

