n, m = list(map(int, input().split()))
e = [set() for i in range(n + 1)]  # khoi tao mang e chua cac tap hop chua dinh ke
# index tu 1 den n tuong ung voi cac dinh
E = []                            # khoi tao mang E chua 2 dinh co quan he
for i in range(m):
    a, b = list(map(int, input().split()))
    E.append((a, b))             # dua (a,b) vao mang chua 2 dinh co qan he
    e[a] |= {b}                   # dua b vao tap hop dinh ke dinh a
    e[b] |= {a}                   # dua a vao tap dinh ke dinh b
    # |= la phep hop tap hop

l = [0] * (n + 1)
for i in range(n + 1):
    l[i] = len(e[i])  # l[i] so dinh ke voi dinh i

lmin = 12000

# xu li
# xet tung cap dinh co quan he (a,b). lay giao cua 2 tap hop e[a],e[b]
# xet tung phan tu x trong tap hop giao xem e[x] co chua a,b hay ko?

for a, b in E:
    t = e[a] & e[b]               # & phep giao tap hop
    for x in t:
        if (a in e[x]) and (b in e[x]):
            w = l[a] + l[b] + l[x] - 6
            if lmin > w:
                lmin = w

print(-1 if lmin == 12000 else lmin)
