(a, b, c, d) = [int(x) for x in input().split()]
e = sorted([a, b, c])
print(max(0, d - (e[1] - e[0])) + max(0, d - (e[2] - e[1])))
