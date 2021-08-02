N, x = list(map(int, input().split()))
a = list(map(int, input().split()))

Sum = 0
if a[0] - x > 0:
    Sum += a[0] - x
    a[0] = x
if a[N - 1] - x > 0:
    Sum += a[N - 1] - x
    a[N - 1] = x
for i in range(1, N):
    d = max(a[i] + a[i - 1] - x, 0)
    a[i] -= d
    Sum += d

print(Sum)
