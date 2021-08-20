n = int(input())
a = set(list('qwertyuiopasdfghjklzxcvbnm'))
al = 0
q = 0
z = 0
for i in range(n):
    k = input().split()
    if k[0] == '.':
        a -= set(list(k[1]))
    elif k[0] == '?':
        a -= set(list(k[1]))
        al += 1
        z += 1
    else:
        a &= set(list(k[1]))
        al += 1
        z += 1
    if len(a) == 1:
        q = i + 1
        break
if len(a) != 1:
    print(0)
else:
    for i in range(q, n):
        k = input().split()
        if k[0] != '.':
            al += 1
    print(al - z - 1)
