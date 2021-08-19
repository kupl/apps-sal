n = int(input())
a = list(map(int, input().split()))
if min(a) >= 0:
    print(n - 1)
    for i in range(1, n):
        print((i, i + 1))
elif max(a) < 0:
    print(n - 1)
    for i in range(1, n)[::-1]:
        print((i + 1, i))
else:
    m = min(a)
    M = max(a)
    if abs(M) >= abs(m):
        idx = a.index(M)
        cnt = 0
        print(2 * n - 2)
        for i in range(2):
            print((idx + 1, 2))
        for i in range(2, n):
            print((i, i + 1))
            print((i, i + 1))
    else:
        idx = a.index(m)
        print(2 * n - 2)
        for i in range(2):
            print((idx + 1, n - 1))
        for i in range(2, n)[::-1]:
            print((i, i - 1))
            print((i, i - 1))
