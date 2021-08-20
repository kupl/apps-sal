from math import sqrt as s
N = int(input())
(x, y) = ([], [])
for i in range(1, int(s(N)) + 1):
    if N % i == 0:
        x.append(i)
        y.append(N // i)
(ans, M) = (float('INF'), len(x))
for i in range(M):
    ans = min(ans, x[i] + y[i] - 2)
print(ans)
