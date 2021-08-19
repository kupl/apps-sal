(x, y) = map(int, input().split())
z = abs(x) + abs(y)
if x > 0 and y > 0:
    print(0, z, z, 0)
elif x > 0 and y < 0:
    print(0, -z, z, 0)
elif x < 0 and y > 0:
    print(-z, 0, 0, z)
elif x < 0 and y < 0:
    print(-z, 0, 0, -z)
