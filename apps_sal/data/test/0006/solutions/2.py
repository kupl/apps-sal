for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    md = me = 0
    for _ in range(n):
        d, h = list(map(int, input().split()))
        md = max(md, d)
        me = max(me, d - h)
    if md >= x:
        print(1)
    elif me:
        print((x - md - 1) // me + 2)
    else:
        print('-1')

