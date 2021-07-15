import sys

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]

s = [a[0]]
sucet = a[0]
for i in range(1, len(a)):
    s.append(s[-1] + a[i])
    sucet += a[i]

if sucet % 3 != 0:
    print(0)
else:
    moznosti = 0
    dvoj = 2*(sucet//3)
    kdedvoj = [(0, 1)[s[0] == dvoj]]
    for i in range(1, len(s)):
        kdedvoj.append(kdedvoj[-1] + (0, 1)[s[i] == dvoj])
    if sucet == 0:
        if kdedvoj[-1] - 2 < 1: print(0)
        elif kdedvoj[-1] - 2 == 1: print(1)
        else: print((kdedvoj[-1]**2 - 3*kdedvoj[-1] + 2)//2)
    else:
        j = n
        for i in range(len(a)):
            if s[i] == sucet//3:
                j = i
                break
        k = -1
        for i in range(len(a)-1, -1, -1):
            if s[i] == sucet:
                k = i
                break
        for i in range(j, k):
            if s[i] == sucet//3:
                moznosti += (kdedvoj[-1] - kdedvoj[i]);
        print(moznosti)
