tests = int(input())
for _ in range(tests):
    (x, y, n) = list(map(int, input().split()))
    f = n // x * x
    if f + y <= n:
        print(f + y)
    else:
        print(f - x + y)
