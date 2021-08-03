n, m = map(int, input().split())
right = True
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print("#", end="")
    else:
        for j in range(m):
            if right:
                if j == m - 1:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if j != 0:
                    print(".", end="")
                else:
                    print("#", end="")
        if right:
            right = False
        else:
            right = True
    print()
