n = int(input())
a = list(map(int, input().split()))
d = set()
t = {}
rep = set()
if a.count(0) >= 2:
    print("cslnb")
    return

for i in a:
    if i in d:
        if t[i] + 1 == 3:
            print("cslnb")
            return
        else:
            t[i] += 1
            rep.add(i)
            if len(rep) >= 2:
                print("cslnb")
                return
    else:
        t[i] = 1
        d.add(i)
if rep:
    for c in rep:
        if c - 1 in d:
            print("cslnb")
            return
s = 0
a.sort()
for i in range(n):
    s += a[i] - i
if s % 2 == 1: print("sjfnb")
else: print("cslnb")
