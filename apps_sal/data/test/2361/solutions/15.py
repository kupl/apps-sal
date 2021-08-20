from math import sqrt
t = int(input())
for q in range(0, t):
    (n, m, k) = list(map(int, input().split()))
    if m <= n // k:
        print(m)
    elif (m - n // k) % (k - 1) == 0:
        print(n // k - (m - n // k) // (k - 1))
    else:
        print(n // k - (m - n // k) // (k - 1) - 1)
