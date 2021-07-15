IN = input
rint = lambda: int(IN())
rmint = lambda: list(map(int, IN().split()))
rlist = lambda: list(rmint())

n, b, a = rmint()
y = a
x = b
d = 0


def ex():
    print(d)
    return


for s in rlist():
    if s:
        if x and y < a:
            y += 1
            x -= 1
        else:
            if y:
                y -= 1
            else:
                if x:
                    x -= 1
                else:
                    ex()
    else:
        if y:
            y -= 1
        else:
            if x:
                x -= 1
            else:
                ex()
    d += 1

print(d)

