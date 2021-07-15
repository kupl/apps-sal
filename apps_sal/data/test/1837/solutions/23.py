input()
a = [int(x) for x in input().split()]

count = 0
m = {}
yes = False
for i, b in enumerate(a):
    if b == i:
        count += 1
    elif not yes:
        if b in m and i == m[b]:
            yes = True
        else:
            m[i] = b
count += 2 if yes else 1 if len(m) else 0
print("%d" % count)

