(N, R) = map(int, input().split())
if N >= 10:
    print(str(R))
else:
    x = R + 100 * (10 - N)
    print(str(x))
