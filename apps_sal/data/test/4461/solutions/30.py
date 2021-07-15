#!/usr/bin/env python3
class V:
    def __init__(self, f, v = None):
        self.f = f
        self.v = v
 
    def __str__(self):
        return str(self.v)
 
    def __call__(self, n):
        if n is None:
            return self.v

        if self.v is None:
            self.v = n
            return self.v
        self.v = self.f(self.v, n) 

h, w = map(int, input().split())

def minmax(*args):
    return max(args) - min(args)

def sep(m, n):
    a = b = c = 0
    nn = n // 2
    ans = V(min, float("inf"))

    for i in range(1, m):
        a = i * n
        mm = (m - i) // 2
    
        # 横
        b, c = (m - i) * nn, (m - i) * (n - nn)
        ans(minmax(a, b, c))

        # 縦
        b, c = mm * n, (m - i - mm) * n
        ans(minmax(a, b, c))
    
    return ans.v

print(min(sep(h, w), sep(w, h)))
