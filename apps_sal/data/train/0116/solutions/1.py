for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x = 0
    for i in l:
        x ^= i
    s = sum(l)
    if s == 2 * x:
        print('0\n')
    elif x == 0:
        print('1')
        print(s)
    else:
        print('2')
        print(x, x + s)
