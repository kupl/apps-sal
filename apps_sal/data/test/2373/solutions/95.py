n = int(input())
P = list(map(int, input().split()))

Cnt = []
cnt = 0
ans = 0
for idx, p in enumerate(P, 1):
    if idx == p:
        Cnt.append(idx)
        cnt += 1
    else:
        cnt = 0
    if cnt == 2:
        ans -= 1
        cnt = 0

ans += len(Cnt)
print(ans)
