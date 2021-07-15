for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if a[i] == 1:
            c += 1
        else:
            break
    if c == n:
        if c % 2 != 0:
            print('First')
        else:
            print('Second')
    else:
        if c % 2 == 0:
            print('First')
        else:
            print('Second')

