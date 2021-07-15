N,M = map(int, input().split())
S = list(input())

cnt,cnt1 = 0,0
for s in S:
    if s == "1":
        cnt1 += 1
    else:
        cnt = max(cnt, cnt1)
        cnt1 = 0
if cnt >= M:
    print(-1)
    return

ans = []
pos = N
while pos > 0:
    for m in range(M, 0, -1):
        if pos - m < 0: continue
        if S[pos - m] == "1": continue

        ans.append(m)
        pos -= m
        break

print(*ans[::-1])
