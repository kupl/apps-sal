n = int(input())
name = input()
dname = dict()
dname[name] = 1
lname = name
for i in range(1, n):
    name = input()
    dname[name] = i + dname[lname]
    lname = name


def l(x):
    return x[1]


sd = sorted(list(dname.items()), key=l, reverse=True)
for i in range(len(sd)):
    print(sd[i][0])
