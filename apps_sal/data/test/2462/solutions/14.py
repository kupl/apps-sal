MIN = 2 * 3 + 2 * 5 + 2 * 7

t = int(input())
for i in range(t):
    n = int(input())
    if n <= MIN:
        print("NO")
    else:
        print("YES")
        if n - MIN in (6, 10, 14):
            print("6 10 15", n - MIN - 1)
        else:
            print("6 10 14", n - MIN)
