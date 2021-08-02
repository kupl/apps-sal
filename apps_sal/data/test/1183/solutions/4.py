for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    l1 = list(map(int, input().split()))
    l1.sort()
    i = 1
    j = 0
    d1 = {}
    for k in l1:
        d1[k] = 1

    while x or i in d1:
        if i in d1:
            i += 1
        else:
            x -= 1
            i += 1

    print(i - 1)
