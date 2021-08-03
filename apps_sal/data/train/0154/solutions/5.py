class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)

        print(horizontalCuts)
        print(verticalCuts)

        maxx = 0
        for x in range(1, len(horizontalCuts)):
            maxx = max(maxx, horizontalCuts[x] - horizontalCuts[x - 1])

        maxy = 0
        for y in range(1, len(verticalCuts)):
            maxy = max(maxy, verticalCuts[y] - verticalCuts[y - 1])

        return (maxx * maxy) % 1000000007
