a = input()
c = []
for i in a:
    c.append(i)
se = set(c)
c.sort()
count = 1
res = []
for i in range(len(c) - 1):
    if c[i] == c[i + 1]:
        count += 1
    else:
        if count % 2 == 0:
            res.append(c[i])
        count = 1
if count % 2 == 0:
    res.append(c[-1])
if len(res) == len(se):
    print("Yes")
else:
    print("No")
