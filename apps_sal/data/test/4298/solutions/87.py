N, D = map(int, input().split())
x = 2 * D + 1

if N % x == 0:
    print(N // x)
else:
    print(N // x + 1)
