IN = input
def rint(): return int(IN())
def rmint(): return map(int, IN().split())
def rlist(): return list(rmint())


n, x, y = rmint()
t = list(map(int, list(IN())))
t.reverse()
t = t[:x]
t[y] = 1 - t[y]
print(sum(t))
