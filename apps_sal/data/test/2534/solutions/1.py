(r, c) = map(int, input().split())
mi = []
m = []
for i in range(r):
    s = list(map(int, input().split()))
    mi.append(min(s))
    m.append(s)
n = []
for i in range(c):
    x = []
    for j in range(r):
        x.append(m[j][i])
    n.append(max(x))
flag = 0
for i in mi:
    if i in n:
        print(i)
        flag = 1
        break
if flag == 0:
    print('GUESS')
