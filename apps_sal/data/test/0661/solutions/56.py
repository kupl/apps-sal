m, k = map(int, input().split())
if m == 0:
    if k == 0:
        print(0, 0)
    else:
        print(-1)
elif m == 1:
    if k == 0:
        print(0, 1, 1, 0)
    else:
        print(-1)
else:
    a = 2 ** m - 1
    if k > a:
        print(-1)
    else:
        for num in range(a + 1):
            if num == k:
                continue
            print(num, end=" ")
        print(k, end=" ")
        for num in range(a, -1, -1):
            if num == k:
                continue
            print(num, end=" ")
        print(k)
