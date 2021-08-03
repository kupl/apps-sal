n, k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)], reverse=True)

m = float('inf')
for i in range(n - k + 1):
    m = min(m, h[i] - h[i + k - 1])

print(m)
