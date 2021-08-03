def getarr(): return(list(map(int, input().split())))


def solve():
    a, b = getarr()
    if (a == b):
        print(0)
    if (a < b):
        diff = abs(a - b)
        if (diff % 2 == 1):
            print(1)
        else:
            print(2)

    if (a > b):
        diff = abs(a - b)
        if (diff % 2 == 0):
            print(1)
        else:
            print(2)


for t in range(int(input())):
    solve()
