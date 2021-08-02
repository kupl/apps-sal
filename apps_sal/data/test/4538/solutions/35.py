N, D = map(int, input().split())

p = 0

for i in range(1, N + 1):
    X, Y = map(int, input().split())
    import math
    c = math.sqrt(X**2 + Y**2)
    if c <= D:
        p += 1

print(p)
