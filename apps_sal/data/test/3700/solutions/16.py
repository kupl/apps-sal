n, k = map(int, input().split())
if k % 2 == 0:
    k = k // 2
    if n - k < k - 1:
        if n - k < 0:
            print(0)
        else:

            print(n - k)
    else:
        if k - 1 < 0:
            print(0)
        else:
            print(k - 1)
else:
    k = k // 2
    if k < n - k:
        if k < 0:
            print(0)
        else:
            print(k)
    else:
        if n - k < 0:
            print(0)
        else:
            print(n - k)
