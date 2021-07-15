n = int(input())

L = [int(x) for x in input().split()]

D = {}

for i in L:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1
        
best = 0

for i in D:
    temp = 0
    for j in range(6):
        temp += D.get(i+j,0)
    best = max(best,temp)
        
print(best)
