class Solution:
    def minJumps(self, arr: List[int]) -> int:
        g = defaultdict(list)
        for i, v in enumerate(arr):
            g[v].append(i)
        N = len(arr)

        val_flag = set()

        cost = [math.inf] * N
        cost[0] = 0
        heap = [(0, 0)]

        while heap:
            c, i = heappop(heap)
            if i == N - 1:
                return c
            for n in (g[arr[i]] * (arr[i] not in val_flag)) + [i - 1, i + 1]:
                if not 0 <= n < N:
                    continue
                if cost[n] > c + 1:
                    cost[n] = c + 1
                    heappush(heap, (c + 1, n))

            val_flag.add(arr[i])
        return cost[-1]
