IN = input
rint = lambda: int(IN())
rmint = lambda: map(int, IN().split())
rlist = lambda: list(rmint())

n, x, y = rmint()
t = list(map(int, list(IN())))
t.reverse()
t = t[:x]
t[y] = 1 - t[y]
print(sum(t))
