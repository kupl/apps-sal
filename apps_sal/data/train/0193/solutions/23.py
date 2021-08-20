class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        H = {}
        for x in arr:
            H[x] = H.get(x, 0) - 1
        L = list(H.values())
        heapq.heapify(L)
        t = 0
        a = 0
        M = len(arr) // 2
        while t < M:
            x = heapq.heappop(L)
            t += -x
            a += 1
        return a
