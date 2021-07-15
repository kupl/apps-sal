a=int(input())
L=[2,1]
for i in range(a-1):
    L.append(L[i]+L[i+1])
print(L[a])
