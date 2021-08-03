import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
A = []
B = []
C = []
D = []
a, b, c, d = 0, 0, 0, 0
for i in range(0, n):
    if s[i] == "a" and t[i] == "a":
        a = a + 1
        A.append(i)
    if s[i] == "a" and t[i] == "b":
        c = c + 1
        C.append(i)
    if s[i] == "b" and t[i] == "a":
        d = d + 1
        D.append(i)
    if s[i] == "b" and t[i] == "b":
        b = b + 1
        B.append(i)

if (c + d) % 2 != 0:
    print(-1)
else:
    print((c + 1) // 2 + (d + 1) // 2)
    lc = len(C)
    ld = len(D)
    while lc >= 2:
        print(str(C[lc - 1] + 1) + " " + str(C[lc - 2] + 1))
        lc = lc - 2
        B.append(lc - 1)
        A.append(lc - 2)
    while ld >= 2:
        print(str(D[ld - 1] + 1) + " " + str(D[ld - 2] + 1))
        ld = ld - 2
        A.append(ld - 1)
        B.append(ld - 2)
    if lc == ld == 1:
        print(str(C[0] + 1) + " " + str(C[0] + 1))
        print(str(C[0] + 1) + " " + str(D[0] + 1))
