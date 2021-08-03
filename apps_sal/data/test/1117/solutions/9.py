def do():
    t = int(input())
    a = [int(x) for x in input().split()]
    cmax = max(a)
    for _ in range(t - 1):
        a = [int(x) for x in input().split()]
        if cmax >= max(a):
            cmax = max(a)
        elif cmax >= min(a):
            cmax = min(a)
        else:
            print('NO')
            return
    print('YES')


do()
