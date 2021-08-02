def fancyfence():
    datain = []
    a = []
    for i in range(int(input())):
        datain.append(int(input()))

    for i in range(3, 1000):
        a.append(((i - 2) * 180) / i)

    for i in datain:
        if i in a:
            print("YES")
        else:
            print("NO")


fancyfence()
