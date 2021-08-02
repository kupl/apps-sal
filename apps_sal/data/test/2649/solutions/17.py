a, b = [], []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    a += [x - y]
    b += [x + y]
print(max(max(a) - min(a), max(b) - min(b)))
