a, b, f, k = [int(i) for i in input().split()]
if (k >= 3):
    if (f > b or 2 * f > b or 2 * (a - f) > b):
        print(-1)
    else:
        fuel = 0
        fwd = 1
        rem = b - f
        while (k != 1):
            if (fwd == 1):
                if (rem >= 2 * (a - f)):
                    rem = rem - 2 * (a - f)
                else:
                    rem = b - 2 * (a - f)
                    fuel += 1
                k -= 1
                fwd = 0
            else:
                if (rem >= 2 * f):
                    rem = rem - 2 * f
                else:
                    rem = b - 2 * f
                    fuel += 1
                k -= 1
                fwd = 1
        if (fwd == 1):
            if (rem >= (a - f)):
                print(fuel)
            else:
                print(fuel + 1)
        else:
            if (rem >= f):
                print(fuel)
            else:
                print(fuel + 1)
elif (k == 1):
    if (f > b or (a - f) > b):
        print(-1)
    else:
        if (b >= a):
            print(0)
        else:
            print(1)
else:
    if (f > b or 2 * (a - f) > b):
        print(-1)
    else:
        fuel = 0
        rem = b - f
        if (rem < 2 * (a - f)):
            rem = b - 2 * (a - f)
            fuel += 1
        else:
            rem = rem - 2 * (a - f)
        if (rem >= f):
            print(fuel)
        else:
            print(fuel + 1)
