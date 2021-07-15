class Solution():
    def __init__(self):
        self.n = int(input())
        self.G = [ int(x) for x in input().strip().split(' ') ]
        self.G.insert(0,0)

        self.used = [0 for i in range(self.n+1)]
        self.dis  = [0 for i in range(self.n+1)]
        self.circle = []
        self.mod = 10**9+7

    def solve(self):
        cur = 1
        for x in range(1,self.n+1):
            if self.used[x]==0:
                circle = self.dfs(x,0,cur)
                if circle is not None:
                    self.circle.append(circle)
                cur += 1

        self.sum = self.n
        self.ans = 1
        mod = self.mod
        for c in self.circle:
            self.ans *= (pow(2,c,mod)-2)%self.mod
            self.sum -= c

        if self.sum == self.n:
            self.ans = pow(2,self.n,mod) - 2
        else:
            self.ans *= pow(2,self.sum,mod)
        self.ans %= self.mod

        return int(self.ans)

    def dfs(self,x,l,cur):
        while True:
            if self.used[x] != 0:
                if self.used[x] == cur:
                    return l - self.dis[x]
                return None
            else:
                self.used[x] = cur
                self.dis[x] = l
                x = self.G[x]
                l += 1

s = Solution()
print(s.solve())

