3
n = int(input())
b = []
f1 = 0
f2 = 0
f0 = 0
f100 = 0
tmp = 0
val = 0
for x in input().split():
    val = int(x)
    if val == 0:
        b.append(val)
        f0 = 1
    elif val == 100:
        b.append(val)
        f100 = 1
    elif val > 0 and val < 10 and (not f1):
        b.append(val)
        f1 = 1
    elif val >= 10 and val < 100 and (val % 10 == 0) and (not f2):
        b.append(val)
        f2 = 1
    else:
        tmp = val
if not f1 and (not f2) and (tmp != 0) and (tmp != 100):
    b.append(tmp)
if len(b) == 0:
    b.append(val)
print(len(b))
for i in range(len(b)):
    print(b[i], end=' ')
print()
