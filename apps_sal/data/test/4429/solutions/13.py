T, = list(map(int, input().split()))
for _ in range(T):
    x, y, z = list(map(int, input().split()))
    if x == z and z >= y:
        print("YES")
        print(y, x, y)
    elif y == z and z >= x:
        print("YES")
        print(x, x, z)
    elif x == y and x >= z:
        print("YES")
        print(x, z, z)
    else:
        print("NO")
