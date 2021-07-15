from collections import deque
class Solution:
    def minDays(self, n: int) -> int:
        day=0
        q=deque([n])
        visited=set()
        while q:
            day+=1
            for _ in range(len(q)):
                v =q.popleft()
                if v==1:
                    return day
                if v%3==0 and v%3 not in visited:
                    q.append(v//3)
                    visited.add(v//3)
                if v%2==0:
                    q.append(v//2)
                    visited.add(v//3)
                if v-1 not in visited:
                    q.append(v-1)
                    visited.add(v-1)
