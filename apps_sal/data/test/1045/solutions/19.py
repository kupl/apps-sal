def kubik(n, l):
    l1 = l
    if n < l * (l + 1) // 2:
        print(l1 - 1)
    else:
        kubik(n - l * (l + 1) // 2, l + 1)


n = int(input())
kubik(n, 0)
