N, R = [int(x) for x in input().split()]
if N >= 10:
    print(R)
else:
    print(100 * (10 - N) + R)
