x, y, z, t1, t2, t3 = list(map(int, input().split()))

tp = abs(x - y) * t1
pt = (abs(x - y) + abs(x - z)) * t2 + t3 + t3 + t3
if tp >= pt:
    print("YES")
else:
    print("NO")
