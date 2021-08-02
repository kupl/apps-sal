n, t = map(int, input().split())
a = list(map(int, input().split()))
print(sum([min(t, a[i] - a[i - 1]) for i in range(1, n)]) + t)
