x, y, z, t1, t2, t3 = list(map(int, input().split()))
lift = (abs(z - x) * t2 + t3 + t3) + (abs(x - y) * t2 + t3)
st = (abs(x - y) * t1)
if (lift <= st):
    print("YES")
else:
    print("NO")
