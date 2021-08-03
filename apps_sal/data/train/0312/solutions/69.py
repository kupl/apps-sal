class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n, store = len(A), [0]
        for x in A:
            store.append(store[-1] + x)
        res = n + 1
        queue = deque()
        for i, x in enumerate(store):
            while queue and x <= store[queue[-1]]:
                queue.pop()
            while queue and x - store[queue[0]] >= K:
                res = min(res, i - queue.popleft())
            queue.append(i)

        return res if res < n + 1 else -1
