class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        rooms_to_visit = [i for i in range(n)]

        def dfs(curr_room, rooms_left, keys):
            if len(rooms_left) == 0:
                return True
            else:
                res = False
                if len(keys) == 0:
                    return False
                for key in keys:
                    if key in rooms_left:
                        rooms_left.remove(key)
                        tmp_keys = keys.union(set(rooms[key])).intersection(set(rooms_left))
                        return dfs(key, rooms_left, tmp_keys)
                        rooms_left.append(key)
        return dfs(0, list(range(1, n)), set(rooms[0]))
