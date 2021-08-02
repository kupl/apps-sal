read = lambda: map(int, input().split())
T = int(input())
for ____ in range(T):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(read()))
    t = 0
    while a:
        b = a[0][0]
        if b >= t:
            t = b
            print('%d ' % t, end='')
        else:
            if t > a[0][1]:
                print('0 ', end='')
                del a[0]
                continue
            else:
                print('%d ' % t, end='')
        t += 1
        del a[0]
    print()
