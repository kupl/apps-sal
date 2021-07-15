n=int(input())
l = [input() for i in range(n)]
L = [[0]*26 for i in range(n)]
s = ''

for i in range(n):
    for j in l[i]:
        L[i][ord(j)-97] += 1

M = L[0]
for k in range(1,n):
    for g in range(26):
        M[g] = min(L[k][g],M[g])

for a in range(26):
    for b in range(M[a]):
        s += chr(a+97)
print(s)
