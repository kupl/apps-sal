a, b, c, d = map(int, input().split())
if abs(a - c) <= d:
    print("Yes")
elif a <= b <= c or c <= b <= a:
    if abs(a - b) <= d and abs(c - b) <= d:
        print("Yes")
    else:
        print("No")
else:
    print("No")
