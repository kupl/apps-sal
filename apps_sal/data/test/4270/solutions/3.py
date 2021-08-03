N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=False)
for i in range(N - 1):
    a[i + 1] = (a[i] + a[i + 1]) / 2

print((a[N - 1]))
