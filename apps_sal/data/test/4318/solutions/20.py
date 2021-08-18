N = int(input())
Hlist = list(map(int, input().split()))

Vcnt = 0
for cnt in range(0, N, 1):
    maxH = max(Hlist[:cnt + 1])
    if Hlist[cnt] >= maxH:
        Vcnt += 1

print(Vcnt)
