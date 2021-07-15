
n = int(input())
A = list(map(int,input().split()))

B = [[0] * 33 for i in range(n)]
C = [0] * 33
for i in range(n):
    t = A[i]
    j = 0
    while t > 0:
        B[i][j] += t%2
        C[j] += B[i][j]
        t//=2
        j += 1

M2 = [1]
for i in range(40):
    M2.append(M2[-1]*2)

S = [0] * n
for i in range(n):
    for j in range(33):
        if B[i][j] == 1:
            if C[j] == 1:
                S[i] += M2[j]

ind = S.index(max(S))
ANS = [A[ind]]
for i in range(n):
    if i != ind:
        ANS.append(A[i])
print(" ".join([str(i) for i in ANS]))
