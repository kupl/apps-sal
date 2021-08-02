l = list(map(int, input().split()))
if l[1] != 100:
    print((l[1] * 100**l[0]))
else:
    print((101 * 100**l[0]))
