for _ in range(int(input())):
    a, c = input().split()
    a = list(a)
    b = sorted(a)
    if a != b:
        for i, x in enumerate(b):
            if a[i] != x:
                tmp = a[i]
                a[i] = x
                break
        for i in range(len(a) - 1, -1, -1):
            if a[i] == x:
                a[i] = tmp
                break
    a = ''.join(a)

    if a < c:
        print(a)
    else:
        print('---')
