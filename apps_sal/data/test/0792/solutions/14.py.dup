H, L, t = 0, 0, 0
n, d = map(int, input().split())
for i in map(int, input().split()):
    if i == 0:
        if H < 0:
            H = d
            t += 1
        L = max(L, 0)
    L += i
    H = min(d, H + i)
    if L > d:
        print(-1)
        return()
print(t)
