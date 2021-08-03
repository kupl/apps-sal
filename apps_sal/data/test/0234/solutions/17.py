T = input().split(' ')
n = int(T[0])
m = int(T[1])
L = []
M = [0] * (m + 2)
L.append(M)
for i in range(n):
    M = [0] * (m + 2)
    t = input()
    for j in range(m):
        if t[j] == '*':
            M[j + 1] = -1
        elif t[j] != '.':
            M[j + 1] = int(t[j])
    L.append(M)
M = [0] * (m + 2)
L.append(M)
c = True
for i in range(1, n + 1):
    for j in range(1, m + 1):
        t = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                if L[i + a][j + b] == -1:
                    t += 1
        if L[i][j] != -1 and L[i][j] != t:
            c = False
            break
if c:
    print("YES")
else:
    print("NO")
