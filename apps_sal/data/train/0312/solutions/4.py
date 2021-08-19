class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        total = 0
        q = deque()
        q.append([-1, 0])

        res = float('inf')
        for i, v in enumerate(A):
            total += v
            # print(q[0])
            while q and total - q[0][1] >= K:
                res = min(res, i - q[0][0])
                q.popleft()

            while q and total < q[-1][1]:
                q.pop()

            q.append([i, total])

        return res if res != float('inf') else -1
