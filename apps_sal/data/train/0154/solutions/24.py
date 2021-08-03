class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        #         m = 0
        #         horizontalCuts.sort()
        #         verticalCuts.sort()
        #         numHoriz = len(horizontalCuts)
        #         numVert = len(verticalCuts)
        #         prevH = 0
        #         for horiz in range(numHoriz + 1):
        #             prevV = 0
        #             for vert in range(numVert + 1):
        #                 if horiz == numHoriz:
        #                     currH = h
        #                 else:
        #                     currH = horizontalCuts[horiz]
        #                 if vert == numVert:
        #                     currV = w
        #                 else:
        #                     currV = verticalCuts[vert]
        #                 m = max(m, (currH - prevH) * (currV - prevV))

        #                 prevV = currV
        #             prevH = currH

        #         return m % (10**9 + 7)
        horizontalCuts.sort()
        verticalCuts.sort()
        prev = 0
        hDiff = 0
        for horiz in horizontalCuts:
            hDiff = max(hDiff, horiz - prev)
            prev = horiz

        hDiff = max(h - prev, hDiff)

        prev = 0
        vDiff = 0
        for vert in verticalCuts:
            vDiff = max(vDiff, vert - prev)
            prev = vert
        vDiff = max(w - prev, vDiff)

        return (vDiff * hDiff) % (10**9 + 7)
