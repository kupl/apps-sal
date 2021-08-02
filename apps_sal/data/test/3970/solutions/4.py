r = input("").split(' ')
x = int(r[0])
y = int(r[1])
l = input("").split(' ')
l = [int(x) for x in l]
l.sort()
k = {}
r = len(l)
for g in range(len(l)):
    if (l[g] % y == 0):
        rk = l[g] // y

        if (rk not in k):
            k[l[g]] = 1
        else:
            r -= 1
    else:
        k[l[g]] = 1
print(r)
