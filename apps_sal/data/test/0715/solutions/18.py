a = input()[2:]
b = input()[2:]
c = input()[2:]
d = input()[2:]
L = [a, b, c, d]
S = 'ABCD'
x = 0
e = []
for i in range(4):
    l = True
    s = True
    for j in range(4):
        if j == i:
            continue
        if len(L[i]) < len(L[j]) * 2:
            l = False
        if len(L[j]) < len(L[i]) * 2:
            s = False
    if l and (not s):
        x += 1
        e.append(i)
    elif s and (not l):
        x += 1
        e.append(i)
if x == 1:
    print(S[e[0]])
else:
    print('C')
