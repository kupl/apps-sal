import numpy as np
class Solution(object):
    def canVisitAllRooms(self, rooms):
        seenRooms = np.zeros(len(rooms), dtype = bool)
        stackKeys = [0]
        while(len(stackKeys)!=0):
            curr = stackKeys.pop()
            if not seenRooms[curr]:
                seenRooms[curr] = True
                for key in rooms[curr]:
                    stackKeys.append(key)
        return True if all(seenRooms) else False
                
            

