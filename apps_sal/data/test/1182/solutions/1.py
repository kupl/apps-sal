# they are all inclusive
R, C, N, K = list(map(int, input().split()))
v = []
for i in range(N):
    v.append(tuple(map(int, input().split())))
ans = 0
for sr in range(1, R + 1):
    for sc in range(1, C + 1):
        for er in range(sr, R + 1):
            for ec in range(sc, C + 1):
                cnt = 0
                for x, y in v:
                    if sr <= x <= er and sc <= y <= ec:
                        cnt += 1
                if cnt >= K:
                    ans += 1
print(ans)
