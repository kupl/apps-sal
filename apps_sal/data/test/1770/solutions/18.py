t = int(input())
for i in range(t):
    n, x, y, d = map(int, input().split())
    if abs(y - x) % d == 0:
        print(abs(y - x) // d)
    else:
        flag = False
        num1, num2 = float("inf"), float("inf")
        if (n - y) % d == 0:
            flag = True
            num1 = (n - y) // d + (n - x) // d + int((n - x) % d != 0)
        if (y - 1) % d == 0:
            flag = True
            num2 = (y - 1) // d + (x - 1) // d + int((x - 1) % d != 0)

        if not flag:
            print(-1)
        else:
            print(min(num1, num2))
