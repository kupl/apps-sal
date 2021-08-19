(N, R) = list(map(int, input().split()))
if N < 10:
    print(100 * (10 - N) + R)
else:
    print(R)
