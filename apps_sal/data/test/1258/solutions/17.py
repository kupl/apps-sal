a = int(input())
A = []
for i in range(a):
    A.append(set())
for i in range(a - 2):
    (x, y, z) = list(map(int, input().split()))
    x -= 1
    y -= 1
    z -= 1
    A[x].add(y)
    A[x].add(z)
    A[y].add(x)
    A[y].add(z)
    A[z].add(x)
    A[z].add(y)
for i in range(len(A)):
    if len(A[i]) == 2:
        k = i
m2 = k
B = [k + 1]
Z = list(A[k])
if len(A[Z[0]]) == 3:
    B.append(Z[0] + 1)
    m1 = Z[0]
else:
    B.append(Z[1] + 1)
    m1 = Z[1]
for i in range(a - 2):
    w = list(A[m1] & A[m2])
    if len(B) > 2:
        if w[0] + 1 != B[-3]:
            B.append(w[0] + 1)
            m2 = int(m1)
            m1 = w[0]
        else:
            B.append(w[1] + 1)
            m2 = int(m1)
            m1 = w[1]
    else:
        B.append(w[0] + 1)
        m2 = int(m1)
        m1 = w[0]
print(*B)
