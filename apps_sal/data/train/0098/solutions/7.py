t = int(input())
while t:
    t = t - 1
    c, m, x = [int(x) for x in input().split(" ")]
    y = min(c, m)
    c = c - y
    m = m - y
    # print("y",y)
    if y <= c + m + x:
        print(y)
    else:
        print((c + m + x + y * 2) // 3)
