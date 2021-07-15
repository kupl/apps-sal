for eps in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    check = [False] * n
    for elem in b:
        check[elem - 1] = True
    b = sorted(a)
    i = 0
    k = 1
    while i < len(a) - 1 and k != 0:
        k = 0
        i = i + 1
        for j in range(len(a) - i):
            if a[j] > a[j + 1] and check[j]:
                k = k + 1
                a[j], a[j + 1] = a[j + 1], a[j]
    if a == b:
        print("YES")
    else:
        print("NO")
