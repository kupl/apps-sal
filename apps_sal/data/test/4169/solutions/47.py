(N, M) = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(N)]
sAB = sorted(AB, key=lambda x: x[0])
ans = 0
cnt = 0
last_cnt = 0
for (a, b) in sAB:
    cnt += b
    if cnt < M:
        ans += a * b
        last_cnt = cnt
    else:
        ans += a * (M - last_cnt)
        break
print(ans)
