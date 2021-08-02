n, m = [int(x) for x in input().split()]
a1 = min(n, m)
a2 = (n + m) // 2 - a1
print(str(a1) + " " + str(a2))
