import sys
n = int(sys.stdin.readline().strip())
s = list(map(int, sys.stdin.readline().strip().split()))
q = int(sys.stdin.readline().strip())
A = [s[:]]
for i in range(1, 20):
    A.append([])
    for j in range(n // 2 ** i):
        A[i].append(A[i - 1][2 * j] + A[i - 1][2 * j + 1])
for i in range(0, q):
    (l, r) = list(map(int, sys.stdin.readline().strip().split()))
    l = l - 1
    r = r - 1
    x = 0
    while l != r + 1:
        l2 = l
        e = 0
        while l2 % 2 == 0 and l + 2 ** (e + 1) <= r + 1:
            l2 = l2 // 2
            e = e + 1
        x = x + A[e][l2]
        l = l + 2 ** e
    print(x // 10)
