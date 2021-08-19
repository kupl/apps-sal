import math
T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    d = False
    A = [0] * n
    for i in range(n):
        A[a[i] - 1] += 1
    ma = max(A)
    man = A.count(ma)
    print((n - man) // (ma - 1) - 1)
