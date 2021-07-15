n = int(input())
T = input().split(' ')
for i in range(n):
    T[i] = int(T[i])
L = []
for i in range(n):
    if T[n-1-i] not in L:
        L.append(T[n-1-i])
print(len(L))
for i in range(len(L)-1):
    print(L[len(L)-1-i], end=' ')
print(L[0])

