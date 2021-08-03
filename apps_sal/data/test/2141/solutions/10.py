n = int(input())
for i in range(n):
    if i % 2 == 0:
        s = "W"
        for j in range(1, n):
            if j % 2 == 1:
                s += "B"
            else:
                s += "W"
    else:
        s = "B"
        for j in range(1, n):
            if j % 2 == 1:
                s += "W"
            else:
                s += "B"
    print(s)
