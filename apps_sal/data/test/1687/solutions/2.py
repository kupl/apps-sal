n, t = int(input()), list(map(int, input().split()))
k = min(t)
print(-1 if any(i % k for i in t) else k)

