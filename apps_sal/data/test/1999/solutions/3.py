n = int(input())
L = input().split(' ')
for i in range(len(L)):
    L[i] = int(L[i])
dico = {}
j = 0
while j < len(L):
    if L[j] not in dico or dico[L[j]] == -1:
        dico[L[j]] = j
        j += 1
    else:
        L[dico[L[j]]] = -1
        dico[L[j]] = -1
        L[j] = L[j] * 2
sm = 0
for i in range(len(L)):
    if L[i] != -1:
        sm += 1
print(sm)
k = 1
for i in range(len(L)):
    if L[i] != -1:
        if k < sm:
            print(L[i], end=' ')
        else:
            print(L[i])
        k += 1
