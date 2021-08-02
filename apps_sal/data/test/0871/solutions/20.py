n, s = [int(x) for x in input().split(" ")]

last = 0
found = False
rng = 2 * s + 2

first = s + 1

f = False

ff = False

for _ in range(n):

    h, m = [int(x) for x in input().split(" ")]
    x = h * 60 + m
    if not f:
        if abs(x - last) >= first:
            found = True
            ff = True
        else:
            last = x
    elif not found:
        if abs(x - last) >= rng:
            found = True
        else:
            last = x
    f = True


# if found:
if ff:
    print(0, 0)
else:
    res = last + s + 1
    print("{} {}".format(res // 60, res % 60))
# else:
#     print()
