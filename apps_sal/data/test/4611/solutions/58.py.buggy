N = int(input())

px = 0
py = 0
pt = 0

for _ in range(N):
    T, X, Y = (int(i) for i in input().split())

    d = abs(X - px + Y - py)
    dt = (T - pt)
    if d > dt or (d % 2) != (dt % 2):
        print('No')
        import sys
        return
    else:
        px = X
        py = Y
        pt = T

print('Yes')
