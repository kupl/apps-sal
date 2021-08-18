N, K = map(int, input().split())

if N % K == 0:
    print(0)
else:
    et = N // K
    a1 = et * K
    a2 = (et + 1) * K
    mi = min(abs(a1 - N), abs(a2 - N))
    print(mi)
