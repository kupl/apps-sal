l = input().split(' ')
n = int(l[0])
k = int(l[1])
m = int(l[2])
L = input().split(' ')
M = input().split(' ')
for i in range(len(M)):
    M[i] = int(M[i])
G = [0] * k
dico = {}
for i in range(k):
    t = input().split(' ')
    G[i] = M[int(t[1]) - 1]
    dico[L[int(t[1]) - 1]] = i
    for j in range(2, len(t)):
        dico[L[int(t[j]) - 1]] = i
        if M[int(t[j]) - 1] < G[i]:
            G[i] = M[int(t[j]) - 1]
s = input().split(' ')
c = 0
for e in s:
    c += G[dico[e]]
print(c)
