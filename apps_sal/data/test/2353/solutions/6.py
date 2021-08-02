n = int(input())

for _ in range(n):
    a, b, c, d = map(int, input().split())
    if a <= b:
        print(b)
        continue
    if c <= d:
        print(-1)
        continue
    print((a - b + c - d - 1) // (c - d) * c + b)
