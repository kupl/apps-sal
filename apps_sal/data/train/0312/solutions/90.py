from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        for ele in A:
            if ele >= k:
                return 1
        s = [0]
        for i in range(len(A)):
            s.append((s[-1] if len(s) else 0) + A[i])
        print(s)
        queue = deque()
        ans = float('inf')
        for i, e in enumerate(s):
            if len(queue) == 0:
                queue.append((i, e))

            elif len(queue) and queue[-1][1] < e:

                if e - queue[0][1] >= k:
                    while len(queue) and e - queue[0][1] >= k:
                        ans = min(ans, i - queue[0][0])
                        queue.popleft()
                queue.append((i, e))

            elif len(queue) and queue[-1][1] >= e:
                while len(queue) and queue[-1][1] >= e:
                    queue.pop()
                queue.append((i, e))

        if len(queue) > 1 and queue[-1][1] >= queue[0][1] + k:
            ans = min(ans, i - queue[-1][0])

        return -1 if ans == float('inf') else ans
