from itertools import accumulate

N, M = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(N)]
sAB = sorted(AB, key=lambda x: x[0])

sB = [sAB[i][1] for i in range(N)]
cum_num = list(accumulate(sB))

num = 0
ans = 0
index_ = -1
for a, b in sAB:
    index_ += 1
    num += b
    if num >= M:
        break
    ans += a * b

if index_ == 0:
    ans += sAB[0][0] * M
else:
    ans += sAB[index_][0] * (M - cum_num[index_ - 1])

print(ans)
