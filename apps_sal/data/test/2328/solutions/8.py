import sys

T = int(sys.stdin.readline().strip())
for t in range (0, T):
    n, k = list(map(int,sys.stdin.readline().strip().split()))
    a = list(map(int,sys.stdin.readline().strip().split()))
    i = 0
    j = k
    M = 10 ** 10
    while j < n:
        if a[j] - a[i] < M:
            M = a[j] - a[i]
            x = (a[j] + a[i]) // 2 + (a[j] + a[i]) % 2
        i = i + 1
        j = j + 1
    print(x)
