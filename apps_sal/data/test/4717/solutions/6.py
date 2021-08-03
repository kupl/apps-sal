a = [int(x) for x in input().split()]
if abs(a[1] - a[0]) > abs(a[2] - a[0]):
    print("B")
else:
    print("A")
