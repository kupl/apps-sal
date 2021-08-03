import sys

n, m = list(map(int, input().split()))
i = k2 = k3 = k6 = 0
while True:
    i += 1
    if i % 6 == 0:
        k6 += 1
    else:
        if i % 3 == 0:
            k3 += 1
        if i % 2 == 0:
            k2 += 1
    k2 = min(n, k2)
    k3 = min(m, k3)
    need = n - k2 + m - k3
    if need <= k6:
        print(i)
        return
