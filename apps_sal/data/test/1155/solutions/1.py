n, m = list(map(int, input().split()))

r = float('inf')
for _ in range(n):
    x, y = list(map(int, input().split()))
    r = min(r, m * x / y)
print(r)
