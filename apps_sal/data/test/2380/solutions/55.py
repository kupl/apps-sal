from itertools import accumulate
(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
BC = [tuple(map(int, input().split())) for _ in range(M)]
A = sorted(A)
BC = sorted(BC, key=lambda x: x[1], reverse=True)
trade = []
len_ = 0
for (b, c) in BC:
    if len_ >= N:
        break
    for _ in range(b):
        if len_ >= N:
            break
        trade.append(c)
        len_ += 1
ans = 0
for i in range(N):
    if i >= len_:
        ans += A[i]
    else:
        ans += max(trade[i], A[i])
print(ans)
