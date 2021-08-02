[x, y, z] = [int(c) for c in input().split()]
if min(y, z) < x:
    print("No")
else:
    print("Yes")
