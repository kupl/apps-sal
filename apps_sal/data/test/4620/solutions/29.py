n = int(input())
csf = [list(map(int, input().split())) for _ in range(n-1)]
ans = []
for i in range(n-1):
    time = 0
    for p in range(i, n - 1):
        c, s, f = csf[p]
        if s >= time:
            time = s+c
        else:
            d = time - s
            time = s + f * (-(-d // f)) + c
    ans.append(time)

ans.append(0)

for i in range(n):
    print((ans[i]))

