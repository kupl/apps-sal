class Solution:
    def minDays(self, n: int) -> int:
        # ret=0
        # while n>=3:
        #     if n%3:
        #         n-=1
        #         ret+=1
        #     else:
        #         n//=3
        #         ret+=1
        # if n==2:
        #     return ret+2
        # if n==1:
        #     return ret+1
        q = deque([(n, 0)])
        seen = {n}
        while q:
            curr, cost = q.popleft()
            if curr == 0:
                return cost
            for nxt in [curr - 1, curr / 3, curr / 2]:
                if nxt != int(nxt):
                    continue
                nxt = int(nxt)
                if nxt in seen:
                    continue
                seen.add(nxt)
                q.append([nxt, cost + 1])
