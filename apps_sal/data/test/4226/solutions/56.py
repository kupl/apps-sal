[X, Y] = [int(i) for i in input().split()]
if 2 * X <= Y and Y <= 4 * X and Y % 2 == 0:
    print("Yes")
else:
    print("No")
