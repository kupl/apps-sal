import itertools
s = [int(x) for x in input().split()]
l = []
a = itertools.product(range(2), repeat=4)
for i in a:
    l.append(i)
for i in range(16):
    cnt = 0
    dnt = 0
    for j in range(4):
        if l[i][j] == 1:
            cnt += s[j]
        else:
            dnt += s[j]
    if cnt == dnt:
        print("Yes")
        return
print("No")
