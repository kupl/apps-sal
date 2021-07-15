N = int(input())
reds = [tuple(map(int, input().split())) for _ in range(N)]
blues = [tuple(map(int, input().split())) for _ in range(N)]

reds.sort(key=lambda x: -x[1])
blues.sort(key=lambda x: x[0])

ans = 0
usedreds = [False]*N
usedblues = [False]*N
for i in range(N):
    if usedreds[i]:
        continue
    a, b = reds[i]
    for j in range(N):
        if usedblues[j]:
            continue
        c, d = blues[j]
        if not (a < c and b < d):
            continue
        ans += 1
        usedreds[i] = True
        usedblues[j] = True
        break

print(ans)
