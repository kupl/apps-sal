n = int(input())
T = input().split(' ')
T.append('1')
t = 0
L = []
for i in range(n):
    if T[i+1] == '1':
        t+=1
        L.append(int(T[i]))
print(t)
for i in range(t-1):
    print(L[i], end=' ')
print(L[-1])

