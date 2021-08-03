a, b, c, d = (int(i) for i in input().split())

if abs(a - c) <= d:
    print("Yes")
elif (abs(a - b) <= d) and (abs(b - c) <= d):
    print("Yes")
else:
    print("No")
