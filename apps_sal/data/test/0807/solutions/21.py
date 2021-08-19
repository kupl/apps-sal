(n, k) = map(int, input().split())
t = list(map(int, input().split()))
p = max([t[i - 1] - t[i] for i in range(1, n)])
print(0 if p < k else p - k)
