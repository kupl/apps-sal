a, b, c, d = map(int, input().split())
tot = a + b + c + d
if tot % 2 == 1:
    print("No")
else:
    if a + b == tot // 2 or a + c == tot // 2 or a + d == tot // 2:
        print("Yes")
    elif a == tot // 2 or b == tot // 2 or c == tot // 2 or d == tot // 2:
        print("Yes")
    else:
        print("No")
