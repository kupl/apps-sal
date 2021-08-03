line = [int(x) for x in input().strip().split(" ")]
a = line[0]
b = line[1]
c = line[2]


def doable(a, b, c):
    for i in range((c // a) + 1):
        t = c - (i * a)
        # print("t: %s" % (t))
        if t % b == 0:
            return True
    return False


if doable(a, b, c):
    print("Yes")
else:
    print("No")
