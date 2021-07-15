
n = int(input())
d = {}

for i in range(n):
    st = input()
    if st in list(d.keys()):
        d[st] += 1
    else:
        d[st] = 1

m = max(list(d.values()))
l = []

for x,y in list(d.items()):
    if y == m:
        l.append(x)
l.sort()

for v in l:
    print(v)


