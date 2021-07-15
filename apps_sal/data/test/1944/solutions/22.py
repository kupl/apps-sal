
def laptops():
    _n = input()
    n = int(_n)
    l = []
    for i in range(n):
        _x, _y = input().split()
        x = int(_x)
        y = int(_y)
        p = (x, y)
        l.append(p)
    l.sort(key=lambda x: x[0])
    for i in range(n-1):
        if l[i][1] > l[i+1][1]:
            print("Happy Alex")
            return
    print("Poor Alex")

laptops()

