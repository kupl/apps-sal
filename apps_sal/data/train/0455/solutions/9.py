
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        coverage = dict()
        for y in range(len(targetGrid)):
            for x in range(len(targetGrid[y])):
                val = targetGrid[y][x]
                if val not in coverage:
                    coverage[val] = (y, x, y, x)
                else:
                    asdf = coverage[val]
                    asdf = (min(asdf[0], y), min(asdf[1], x), max(asdf[2], y), max(asdf[3], x))
                    coverage[val] = asdf
        print(coverage)
        before = dict()
        done = set()
        for color in coverage:
            asdf = coverage[color]
            s = set()
            for y in range(asdf[0], asdf[2] + 1):
                for x in range(asdf[1], asdf[3] + 1):
                    s.add(targetGrid[y][x])
                if color in s:
                    s.remove(color)
            before[color] = s
        print(before)

        while len(before) > 0:
            gotOne = False
            for color in list(before.keys()):
                dependencies = before[color]
                dependencies = dependencies - done
                if len(dependencies) == 0:
                    before.pop(color)
                    done.add(color)
                    gotOne = True
                else:
                    before[color] = dependencies
            if gotOne == False:
                return False
        return True
