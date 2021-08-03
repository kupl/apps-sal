N, R = list(map(int, input().split()))
if N >= 10:
    print(R)
else:
    K = 10 - N
    I = 100 * K
    print((R + I))
