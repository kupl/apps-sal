(x, y, z, t1, t2, t3) = map(int, input().split(' '))


diff = abs(x - y)
diffe = abs(z - x)

elevator = diffe * t2 + diff * t2 + 3 * t3
walk = diff * t1

if elevator <= walk:
    print("YES")
else:
    print("NO")
