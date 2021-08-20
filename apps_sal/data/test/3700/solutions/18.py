(n, k) = (int(x) for x in input().split())
if n >= k - 1:
    print((k - 1) // 2)
    quit()
elif k % 2 == 0:
    if n <= k // 2:
        print(0)
        quit()
    else:
        print(n - k // 2)
        quit()
elif n <= k // 2:
    print(0)
    quit()
else:
    print(n - k // 2)
    quit()
