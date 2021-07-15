n = int(input())
T = input().split(' ')
for i in range(n):
    T[i] = int(T[i])
D = {}
for i in range(n):
    D[T[i]] = 0
for i in range(n):
    if T[i]-1 not in D:
        D[T[i]] = 1
    else:
        D[T[i]] = D[T[i]-1] + 1
m = -1
j = -1
for i in D:
    if D[i] > m:
        m = D[i]
        j = i
L = []
for i in range(n-1, -1, -1):
    if T[i] == j:
        L.append(i)
        j -= 1
print(m)
for i in range(m-1):
    print(L[m-1-i]+1, end=' ')
print(L[0]+1)

