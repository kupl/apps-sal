def foo():
    n = int(input())
    h = [int(input()) for i in range(0, n)]
    curX = 0
    res = 0
    for x in h:
        if x < curX:
            res += curX - x
            curX = x
        res += x - curX
        curX = x
        res += 2
    print(res - 1)


foo()
