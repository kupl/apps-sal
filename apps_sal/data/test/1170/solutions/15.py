def test(x):
    i = 1
    flag = False
    while i**2 < x:
        if x % i == 0:
            a, b = i, x // i
            if (a + b) % 2 == 0:
                z = (a + b) // 2
                y = b - z
                u = z // y
                if (z // u == y):
                    y = u
                    flag = True
                    break
        i += 1
    if flag:
        print(str(z) + " " + str(y))

    else:
        if x == 0:
            print("1 1")
        else:
            print("-1")


n = int(input())
for j in range(n):
    test(int(input()))
