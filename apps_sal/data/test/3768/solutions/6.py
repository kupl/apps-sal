a = input().split()
target = (int(a[0]), int(a[1]))
x = (1, 0)
y = (0, 1)
toadd = "A"
ans = ""


def less(a, b):
    return a[0] * b[1] < b[0] * a[1]


while True:
    z = (x[0] + y[0], x[1] + y[1])
    if z[0] > target[0] or z[1] > target[1]:
        print("Impossible")
        return
    if z == target:
        print(ans)
        return
    if less(z, target):  # z replaces y
        low = 1
        high = int(1e18)
        while (high > low):
            guess = (low + high + 1) // 2
            if less((x[0] * guess + y[0], x[1] * guess + y[1]), target):
                low = guess
            else:
                high = guess - 1
        ans += str(low)
        ans += "A"
        y = (y[0] + low * x[0], y[1] + low * x[1])
    elif less(target, z):
        low = 1
        high = int(1e18)
        while (high > low):
            guess = (low + high + 1) // 2
            if less(target, (x[0] + guess * y[0], x[1] + guess * y[1])):
                low = guess
            else:
                high = guess - 1
        ans += str(low)
        ans += "B"
        x = (x[0] + low * y[0], x[1] + low * y[1])
    else:
        print("Impossible")
        return
