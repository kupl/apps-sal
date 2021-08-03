a = int(input())
sp = []
for i in range(a):
    sp += [[int(input()), i]]
sp.sort()
w = 1
le = 0
i = 0
w2 = ''
while le <= sp[-1][0]:
    w2 = w2 + str(w)
    if sp[i][0] <= le + len(w2):
        while i < a and sp[i][0] <= le + len(w2):
            sp[i] = [sp[i][1], [w2[sp[i][0] - le - 1]]]
            i += 1
    le += len(w2)
    w += 1
sp.sort()
for t in range(a):
    print(*sp[t][1])
