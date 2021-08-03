from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        c_all, visited = Counter(tiles), set()
        stack = [(x, Counter([x])) for x in c_all]

        while stack:
            element, c = stack.pop()
            if element not in visited:
                stack.extend([(element + x, c + Counter([x])) for x in c_all - c])
                visited.add(element)

        return len(visited)
