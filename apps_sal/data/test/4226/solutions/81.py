x, y = map(int, input().split())
if y % 2 == 0 and x * 4 - y >= 0 and -x * 2 + y >= 0:
    print("Yes")
else:
    print("No")
