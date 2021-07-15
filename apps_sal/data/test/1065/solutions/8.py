n,k,M,D = input().split()
n = int(n)
k = int(k)
M = int(M)
D = int(D)
low = (n + k * D - 1) // (k * D)
high = M
i = 1
an = 0
while i <= D:
    lo = low-1
    hi = high
    while lo != hi:
        mi = (lo + hi + 1) // 2
        if (i-1)*k*mi + mi <= n:
            lo = mi
        else:
            hi = mi - 1
    if lo != low - 1 and an < lo * i:
        an = lo * i
    i = i + 1
print(an)
