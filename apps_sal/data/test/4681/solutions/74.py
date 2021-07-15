n = int(input())

L0, L1 = 2, 1
if n == 1:
    print(L1)
else:
    for _ in range(n - 1):
        L = L0 + L1
        L0, L1 = L1, L
    print(L)
