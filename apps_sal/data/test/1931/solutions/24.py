"""


5
3
14
15
24
1



"""
n = int(input())
L = [2, 7]
S = 8
for i in range(1, 100000):
    L.append(L[i] + S)
    S += 3
for i in range(0, n):
    o = int(input())
    tot = 0
    while 1:
        I = 0
        V = -1
        J = len(L) - 1
        while I <= J:
            m = (I + J) // 2
            if L[m] > o:
                J = m - 1
            else:
                V = m
                I = m + 1
        if V != -1:
            tot += 1
            o -= L[V]
        else:
            break
    print(tot)
