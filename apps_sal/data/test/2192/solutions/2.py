import math

def cmp(a):
    return a[1]*10000+a[0]

n = int(input())
W =  [list(map(float, input().split(' '))) for i in range(n)]

A = [[0 for i in range(n)] for j in range(n)]
B = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i!=j:
            if i>j:
                S = W[i][j]
                R = W[j][i]
                det = -2
                detA = -S-R
                detB = R-S
                a = detA/det
                b = detB/det
                A[i][j] = a
                A[j][i] = a
                B[i][j] = b
                B[j][i] = -b
        else:
            A[i][j] = W[i][j]
            B[i][j] = 0

s = ""
for i in range(n):
    for j in range(n):
        s+=str(A[i][j])+" "
    s+="\n"

print(s)


s = ""
for i in range(n):
    for j in range(n):
        s+=str(B[i][j])+" "
    s+="\n"

print(s)
