x, y, z = map(int, input().split())
a, b, c = map(int, input().split())
if x > a or ((a + b) - x) < y or ((a + b + c) - x - y) < z:
    print("NO")
else:
    print("YES")
