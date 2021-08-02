x, y, z = list(map(int, input().split()))
a, b, c = list(map(int, input().split()))
if a >= x and a + b >= x + y and a + b + c >= x + y + z:
    print("YES")
else:
    print("NO")
