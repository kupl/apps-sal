x, y, z = list(map(int, input().split()))
a, b, c = list(map(int, input().split()))
a -= x
if a < 0:
    print("NO")
    return
if a + b < y:
    print("NO")
    return
if a + b + c - y < z:
    print("NO")
    return
print("YES")
