for kek in range(int(input())):
    (n, x) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        f = 0
        if  x % a[i] != 0:
            f += 1
        a[i] = x // a[i] + f
    a.sort()
    ans = 0
    com = 1
    for i in a:
        if i == com:
            ans += 1
            com = 1
        else:
            com += 1
    print(ans)
