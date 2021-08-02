from collections import Counter


N, M = [int(x) for x in input().split()]
Cnter = Counter([int(x) for x in input().split()])
for i in range(M):
    b, c = [int(x) for x in input().split()]
    Cnter[c] += b
V = sorted(list(Cnter.most_common()))
cnt = 0
ans = 0
for v in V[::-1]:
    ans += v[0] * min(v[1], N - cnt)
    cnt += v[1]
    if cnt >= N:
        break
print(ans)
