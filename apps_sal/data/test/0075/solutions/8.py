st = input()
tmp = st.split(' ')
m = int(tmp[0])
n = int(tmp[1])
mapp = []
oc = []
for i in range(m):
    tmp = input()
    mapp.append(tmp)
    for j in range(n):
        if tmp[j] != '.':
            oc.append((i, j))
for x in range(m):
    for y in range(n):
        for i in oc:
            if i[0] != x and i[1] != y:
                break
        else:
            print('YES')
            print(x + 1, y + 1)
            return
else:
    print('NO')
