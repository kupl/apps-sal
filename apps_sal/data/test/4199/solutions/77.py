(n, k) = map(int, input().split())
h = list(map(int, input().split()))
print(len([h[i] for i in range(n) if h[i] >= k]))
