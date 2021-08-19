from itertools import accumulate
INF = float('inf')
N = int(input())
A = [int(x) for x in input().split()]
cumA = list(accumulate(A))
ans = INF
for i in range(N - 1):
    x = cumA[i]
    y = cumA[N - 1] - cumA[i]
    ans = min(ans, abs(x - y))
print(ans)
