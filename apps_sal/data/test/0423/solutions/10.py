n, k = map(int, input().split(" "))
mas = [-100000000000000] * (n + 1)
d = 0
limit = 10**10
for i in range(n + 1):
    s = input()
    if s == "?":
        d += 1
    else:
        mas[i] = int(s)
if k == 0 and mas[0] == 0:
    print("Yes")
elif k == 0 and mas[0] != 0:
    if mas[0] == -100000000000000:
        if (n - d) % 2 != 0:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
else:
    if d != 0:
        if n % 2 == 0:
            print("No")
        else:
            print("Yes")
    else:

        b = mas[n]
        for i in range(n - 1, 0, -1):
            b = (mas[i] + b * k)
            if abs(b) > limit:
                print("No")
                break
        else:
            print("Yes") if (b * k == -mas[0]) else print("No")
