from bisect import bisect_left

Q = int(input())
K = [int(input()) for _ in range(Q)]
M = 10**5

L = [None for _ in range(M + 1)]
R = [None for _ in range(M + 1)]
L[0] = 0
R[0] = 0
for n in range(1, M + 1):
    for k in range(5):
        if 10**k <= n < 10**(k + 1):
            L[n] = L[n - 1] + k + 1
            R[n] = R[n - 1] + L[n]
            break

for num in K:
    i = bisect_left(R, num)
    a = num - R[i - 1]
    n = 0
    for q in range(1, L[i] + 1):
        for j in range(6):
            if 10**j <= q < 10**(j + 1):
                k = j + 1
                break
        if n + k >= a:
            break
        n += k
    print(str(q)[a - n - 1])
