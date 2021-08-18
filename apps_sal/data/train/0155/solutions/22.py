import collections


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        outEdges = {}
        inEdges = {}

        for idx, height in enumerate(arr):

            jumpRangeRight = list(range(idx + 1, min(len(arr), idx + d + 1)))
            jumpRangeLeft = list(range(idx - 1, max(0, idx - d) - 1, -1))

            for jumpRange in [jumpRangeLeft, jumpRangeRight]:
                for jumpIdx in jumpRange:
                    if arr[jumpIdx] >= arr[idx]:
                        break

                    if idx not in outEdges:
                        outEdges[idx] = set()
                    outEdges[idx].add(jumpIdx)

                    if jumpIdx not in inEdges:
                        inEdges[jumpIdx] = set()
                    inEdges[jumpIdx].add(idx)

        noInEdges = collections.deque()
        for idx in range(len(arr)):
            if idx not in inEdges:
                noInEdges.append(idx)

        topologicalOrder = collections.deque()
        while noInEdges:
            idx = noInEdges.pop()
            topologicalOrder.append(idx)
            if idx not in outEdges:
                continue
            for jumpIdx in outEdges[idx]:
                inEdges[jumpIdx].remove(idx)
                if not inEdges[jumpIdx]:
                    noInEdges.append(jumpIdx)

        maxJumps = 1
        jumpCount = [1] * len(arr)
        while topologicalOrder:
            idx = topologicalOrder.popleft()

            if idx not in outEdges:
                continue

            for jumpIdx in outEdges[idx]:
                jumpCount[jumpIdx] = max(jumpCount[idx] + 1, jumpCount[jumpIdx])
                maxJumps = max(jumpCount[jumpIdx], maxJumps)

        return maxJumps

    def maxJumpsBfs(self, arr: List[int], d: int) -> int:
        bfs = collections.deque()

        for idx in range(len(arr)):
            bfs.append((idx, 1))

        stepCount = {}
        maxSteps = 0

        while bfs:
            idx, steps = bfs.popleft()

            if idx in stepCount and steps <= stepCount[idx]:
                continue
            stepCount[idx] = steps

            maxSteps = max(steps, maxSteps)

            for jumpIdx in range(idx + 1, min(len(arr), idx + d + 1)):
                if arr[jumpIdx] >= arr[idx]:
                    break

                bfs.append((jumpIdx, steps + 1))

            for jumpIdx in range(idx - 1, max(0, idx - d) - 1, -1):
                if arr[jumpIdx] >= arr[idx]:
                    break

                bfs.append((jumpIdx, steps + 1))

        return maxSteps
