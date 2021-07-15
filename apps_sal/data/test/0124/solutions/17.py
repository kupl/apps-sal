x, y, z = [int(x) for x in input().split()]
a, b, c = [int(x) for x in input().split()]
if a < x:
    print("NO")
    return
a -= x
b += a
if b < y:
    print("NO")
    return
b -= y
c += b
if c < z:
    print("NO")
    return
print("YES")
