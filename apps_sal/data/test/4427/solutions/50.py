(r, d, x) = map(int, input().split())
A = x
for _ in range(10):
    A = r * A - d
    print(A)
