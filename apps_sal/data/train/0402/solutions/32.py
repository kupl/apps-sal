class Solution:

    def isEscapePossible(self, b: List[List[int]], s: List[int], t: List[int]) -> bool:

        def find(source, target, blocked):
            queue = [source]
            visited = set()
            while queue:
                (x, y) = queue.pop()
                if len(visited) > 20000:
                    return True
                if x == target[0] and y == target[1]:
                    return True
                visited.add((x, y))
                next_options = []
                for (x_delta, y_delta) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    (new_x, new_y) = (x + x_delta, y + y_delta)
                    if new_x < 0 or new_x >= 10 ** 6 or new_y < 0 or (new_y >= 10 ** 6):
                        continue
                    if (new_x, new_y) in visited or (new_x, new_y) in blocked:
                        continue
                    next_options.append((new_x, new_y))
                next_options.sort(key=lambda point: (point[0] - target[0]) ** 2 + (point[1] - target[1]) ** 2, reverse=True)
                queue += next_options
            return False
        bl = set()
        for bi in b:
            bl.add(tuple(bi))
        return find(s, t, bl) and find(t, s, bl)
