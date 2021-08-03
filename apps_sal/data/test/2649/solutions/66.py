n = int(input())
a, b = [], []

for _ in range(n):
    x, y = list(map(int, input().split()))
    a.append(x - y)
    b.append(x + y)

ans = max(max(a) - min(a), max(b) - min(b))
print(ans)
