import sys
t = int(input())
for i in range(t):
    (n, k) = list(map(int, sys.stdin.readline().strip().split()))
    a = list(map(int, sys.stdin.readline().strip().split()))
    x = [0] * n
    for j in range(1, n - 1):
        if a[j] > a[j - 1] and a[j] > a[j + 1]:
            x[j] = 1
    k = k - 2
    op = 0
    curr = 0
    curr = sum(x[:k])
    op = curr
    op1 = 1
    for j in range(k, n):
        curr = curr + x[j] - x[j - k]
        if curr > op:
            op1 = j - k + 1
            op = curr
    op = max(op, curr)
    print(op + 1, op1)
