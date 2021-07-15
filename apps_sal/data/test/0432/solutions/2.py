input()
c = list(map(int, input().split()))
a = list(map(int, input().split()))

u = [0] * len(a)

ans = 0

for i in range(len(a)):
    if u[i] != 0:
        continue
    idx = i
    while u[idx] == 0:
        u[idx] = 1
        idx = a[idx] - 1
    
    if (u[idx] == 2):
        idx = i
        while u[idx] == 1:
            u[idx] = 2
            idx = a[idx] - 1
        continue

    start = idx
    mn = c[idx]
    u[idx] = 2
    while a[idx] - 1 != start:
        idx = a[idx] - 1
        mn = min(mn, c[idx])
        u[idx] = 2

    idx = i
    while u[idx] == 1:
        u[idx] = 2
        idx = a[idx] - 1
    ans += mn
print(ans)
