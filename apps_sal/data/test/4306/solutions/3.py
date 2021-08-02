a = [int(x) for x in input().split()]
print(max(0, min(a[1], a[3]) - max(a[0], a[2])))
