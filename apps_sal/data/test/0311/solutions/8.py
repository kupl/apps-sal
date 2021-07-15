x, y, z, t1, t2, t3 = list(map(int, input().split()))
dp = abs(x - y) * t1;
dl = abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3;
if dp < dl:
    print("NO")
else:
    print("YES")

