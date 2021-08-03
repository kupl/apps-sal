IN = input
def rint(): return int(IN())
def rmint(): return list(map(int, IN().split()))
def rlist(): return list(rmint())


n = rint()
a = rlist()
a.sort()
k = 1
for c in a:
    if c >= k:
        k += 1
print(k - 1)
