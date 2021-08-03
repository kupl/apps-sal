n = int(input())

a = [10**9, 0, 0, 0]

L = list(map(int, input().split()))
T = []
for i in range(n):
    if(L[i] == 1):
        T.append([i + 1])
ind = 0
for i in range(n):
    if(L[i] == 2 and ind < len(T)):
        T[ind].append(i + 1)
        ind += 1
ind = 0
for i in range(n):
    if(L[i] == 3 and ind < len(T) and len(T[ind]) == 2):
        T[ind].append(i + 1)
        ind += 1
print(ind)
for i in range(ind):
    item = T[i]
    print(item[0], item[1], item[2])
