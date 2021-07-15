n, k = list(map(int, input().split()))
if k == 1:
    print(n)
else:
    i = 0
    while 2 ** (i + 1) <= n:
        i += 1
    ans = 2 ** (i + 1) - 1
    print(ans)

