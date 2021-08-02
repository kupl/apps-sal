N, M = map(int, input().split())
a = [0] * (max(N, M) + 1)
a[0] = 1
a[1] = 1
for i in range(2, len(a)):
    a[i] = i * a[i - 1] % 1000000007

if N == M:
    print(a[N] * a[M] * 2 % 1000000007)
elif abs(N - M) == 1:
    print(a[N] * a[M] % 1000000007)
else:
    print(0)
