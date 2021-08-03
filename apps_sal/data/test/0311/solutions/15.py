x, y, z, t1, t2, t3 = map(int, input().split())
time1 = abs(x - y) * t1
time2 = (abs(x - y) + abs(z - x)) * t2 + 3 * t3
if time2 <= time1:
    print("YES")
else:
    print("NO")
