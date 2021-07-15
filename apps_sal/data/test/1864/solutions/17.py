r = lambda: input()
ri = lambda: int(r())
rr = lambda: map(int, r().split())
rl = lambda: list(rr())

n = ri()
a = rl()

if 1 in a:
    print(-1)
else:
    print(1)
