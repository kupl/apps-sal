import sys
sys.setrecursionlimit(10 ** 6)

N, X = list(map(int, input().split()))

h = [1]
p = [1]

for _ in range(50):
    h.append(h[-1] * 2 + 3)
    p.append(p[-1] * 2 + 1)

def bug(l, y):
    if l == 0:
        return 0 if y <= 0 else 1
    
    mid = (h[l] + 1) // 2
    if y < mid:
        return bug(l - 1, y - 1)
    elif y == mid:
        return p[l - 1] + 1
    elif y > mid:
        return p[l - 1] + 1 + bug(l - 1, y - mid)
    
print((bug(N, X)))

