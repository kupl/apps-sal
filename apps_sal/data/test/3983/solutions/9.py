import sys
readline = sys.stdin.readline

class UF():
    def __init__(self, num):
        self.par = [-1]*num
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            stack = []
            while self.par[x] >= 0:
                stack.append(x)
                x = self.par[x]
            for xi in stack:
                self.par[xi] = x
            return x
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] > self.par[ry]:
                rx, ry = ry, rx
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
            return True
        return False

T = int(readline())
Ans = [None]*T
for qu in range(T):
    N, M = list(map(int, readline().split()))
    Edge = [tuple([int(x)-1 for x in readline().split()]) for _ in range(M)]
    if N&1:
        res = N*(N-1)//2 - M
        if res & 1:
            Ans[qu] = 'First'
        else:
            Ans[qu] = 'Second'
        continue
    else:
        T = UF(N)
        for u, v in Edge:
            T.union(u, v)
         
        S = set([T.find(0), T.find(N-1)])
        odd = 0
        even = 0
        parity = (N*(N-1)//2 - M - T.par[T.find(0)])%2
        parity2 = (N*(N-1)//2 - M - T.par[T.find(N-1)])%2
        if parity != parity2:
            Ans[qu] = 'First'
            continue
        for i in range(N):
            ri = T.find(i) 
            if ri in S:
                continue
            S.add(ri)
            if -T.par[ri] & 1:
                odd += 1
            else:
                even += 1
        if parity & 1 == 0:
            if odd%4 == 0:
                ans = 0
            elif odd%4 == 1:
                ans = 1
            elif odd%4 == 2:
                if not even & 1:
                    ans = 0
                else:
                    ans = 0
            else:
                if not even & 1:
                    ans = 1
                else:
                    ans = 1
        else:
            if odd%4 == 0:
                ans = 1
            elif odd%4 == 1:
                ans = 1
            elif odd%4 == 2:
                if not even & 1:
                    ans = 1
                else:
                    ans = 1
            else:
                if not even & 1:
                    ans = 1
                else:
                    ans = 0
            
        Ans[qu] = 'First' if ans else 'Second'
        
            
print(('\n'.join(Ans)))

