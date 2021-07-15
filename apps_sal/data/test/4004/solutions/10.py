IN = input
rint = lambda: int(IN())
rmint = lambda: list(map(int, IN().split()))
rlist = lambda: list(rmint())

n = rint()
a = rlist()
b = list(set(a))
b.sort()
if len(b) > 3:
    print(-1)
elif len(b) == 1:
    print(0)
elif len(b) == 2:
    p = b[1] - b[0]
    if p&1:
        print(p)
    else:
        print(p//2)
else:
    if b[1]-b[0] == b[-1]-b[1]:
        print(b[1]-b[0])
    else:
        print(-1)

