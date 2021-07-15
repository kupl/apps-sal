from collections import deque

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        rs = [0]
        for n in A: rs.append(rs[-1]+n)
        print(rs)
        q = deque()
        mn = float('inf')
        for i,s in enumerate(rs):
            while q and s <= rs[q[-1]]:
                q.pop()
            while q and s-rs[q[0]] >= K:
                mn = min(mn,i-q.popleft())
            q.append(i)
        return mn if mn != float('inf') else -1
