class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        res, dire, all_keys = 0, [[0, 1], [1, 0], [0, -1], [-1, 0]], 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    loc = (i, j)
                if grid[i][j] in 'abcdef':
                    all_keys += 1
        cur, seen = set([(loc, ())]), set([(loc, ())])

        def checker(loc, keys, di):
            x, y = loc[0] + di[0], loc[1] + di[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                t = grid[x][y]
                if t in '@.' or (t in keys) or (t in 'ABCDEF' and str.lower(t) in keys):
                    return ((x, y), keys), False
                if t in 'abcdef':
                    newkeys = tuple(sorted(set(list(keys) + [t])))
                    if len(newkeys) == all_keys:
                        return True, True
                    return ((x, y), newkeys), False
            return False, False
        while cur:
            res, tmp = res + 1, []
            for node in cur:
                loc, keys = node
                for di in dire:
                    new_node, state = checker(loc, keys, di)
                    if state:
                        return res
                    if new_node not in seen and new_node:
                        tmp += [new_node]
            cur = set(tmp)
            seen |= cur
        return -1
