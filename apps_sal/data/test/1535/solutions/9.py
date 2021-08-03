def ans():
    n, x0, y0 = [int(i) for i in input().split()]
    ans = []
    for i in range(n):
        x, y = [int(i) for i in input().split()]
        if x == x0:
            ans.append("s")
        else:
            ans.append(float(y - y0) / float(x - x0))

    print(len(set(ans)))

    return


ans()
