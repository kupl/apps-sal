n, m = list(map(int, input().split()))
v = sorted(list(map(int, input().split())))
print(min(v[i + n - 1] - v[i] for i in range(0, len(v) - n + 1)))
