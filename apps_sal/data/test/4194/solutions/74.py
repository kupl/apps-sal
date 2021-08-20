import sys
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
sum_day = sum(A)
ans = N - sum_day
if ans < 0:
    print(-1)
else:
    print(ans)
