class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        i = 0
        pow2Dict = {1: 0}
        pow2Now = 1
        while i < 32:
            i += 1
            pow2Now *= 2
            pow2Dict[pow2Now] = i
        visited = {}
        stack = [(0, i, i) for i in range(lo, hi + 1)]
        while stack:
            (stepNow, numNow, numOrigin) = heapq.heappop(stack)
            if numNow in pow2Dict:
                visited[numOrigin] = stepNow + pow2Dict[numNow]
            elif numNow in visited:
                visited[numOrigin] = stepNow + visited[numNow]
            elif numNow % 2:
                heapq.heappush(stack, (stepNow + 1, numNow * 3 + 1, numOrigin))
            else:
                heapq.heappush(stack, (stepNow + 1, numNow // 2, numOrigin))
        sortedNums = sorted([i for i in range(lo, hi + 1)], key=lambda x: (visited[x], x))
        return sortedNums[k - 1]
