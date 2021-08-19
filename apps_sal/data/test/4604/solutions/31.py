n = int(input())
a = list(map(int, input().split()))
flg = 0
a.sort()
if n % 2 == 0:
    if a[0] == 1 and a[1] == 1:
        for i in range(2, n, 2):
            if a[i] == a[i + 1] and a[i - 1] + 2 == a[i]:
                continue
            else:
                flg = 1
                break
    else:
        flg = 1
elif a[0] == 0:
    for i in range(1, n, 2):
        if a[i] == a[i + 1] and a[i - 1] + 2 == a[i]:
            continue
        else:
            flg = 1
            break
else:
    flg = 1
if flg == 1:
    print(0)
else:
    print(2 ** (n // 2) % (10 ** 9 + 7))
