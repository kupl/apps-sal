class Solution:
    @lru_cache()
    def minDays(self, n: int) -> int:
        q = deque()
        q.append(n)
        v = set()
        ans = 0
        while(len(q)):
            l = len(q)
            for _ in range(l):
                x = q.popleft()
                if(x - 1 == 0):
                    ans = ans + 1
                    return ans
                if(x % 3 == 0 and x // 3 not in v):
                    v.add(x)
                    q.append(x // 3)
                if(x % 2 == 0 and x // 2 not in v):
                    v.add(x)
                    q.append(x // 2)
                if(x - 1 not in v):
                    v.add(x)
                    q.append(x - 1)
            ans += 1

        return ans
