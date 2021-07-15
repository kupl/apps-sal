import math
for _ in range(int(input())):
    s = list(input())
    l = len(s)
    f = [0 for _ in range(l+1)]
    cp = 0
    cn = 0
    for i in range(l):
        if s[i] == '+':
            cp += 1
        else:
            cn += 1
        if (cn-cp)>0 and f[cn-cp] == 0:
            f[cn-cp] = i+1
    print(sum(f)+l)
