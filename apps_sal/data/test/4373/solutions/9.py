IN = input
rint = lambda: int(IN())
rmint = lambda: list(map(int, IN().split()))
rlist = lambda: list(rmint())

n = rint()
a = rlist()
a.sort()
k = 1
for c in a:
    if c >= k: k += 1
print(k - 1)
