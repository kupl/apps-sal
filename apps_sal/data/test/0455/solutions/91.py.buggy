N, *XY = map(int, open(0).read().split())
XY = list(zip(*[iter(XY)] * 2))

mod = sum(XY[0]) % 2
if any((x + y) % 2 != mod for x, y in XY):
    print(-1)
    return

D = [2 ** i for i in reversed(range(32))] + [1] * (mod == 0)
print(len(D))
print(*D)

for x, y in XY:
    A = []
    for d in D:
        if 0 <= x - y and 0 <= x + y:
            A.append("R")
            x -= d
        elif x - y < 0 and 0 <= x + y:
            A.append("U")
            y -= d
        elif 0 <= x - y and x + y < 0:
            A.append("D")
            y += d
        else:
            A.append("L")
            x += d

    print("".join(A))
