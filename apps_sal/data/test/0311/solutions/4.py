x, y, z, t1, t2, t3 = [int(i) for i in input().split()]
if abs(z - x) * t2 + 3 * t3 + abs(x - y) * t2 <= abs(x - y) * t1:
    print("YES")
else:
    print("NO")
