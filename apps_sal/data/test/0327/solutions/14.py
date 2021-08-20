(n, k) = map(int, input().split())
if k == 1:
    print(n)
else:
    pr = 1
    while pr <= n:
        pr *= 2
    print(pr - 1)
