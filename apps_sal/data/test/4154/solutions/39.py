N,M = map(int,input().split())
L = []
R = []
for i in range(M):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)

a = 1
b = N

for i in range(M):
    if(L[i] >= a and R[i] >= b):
        a = L[i]
    if(L[i] <= a and R[i] <= b):
        b = R[i]
    if(L[i] >= a and R[i] <= b):
        a = L[i]
        b = R[i]
    if(R[i] < a or L[i] > b):
        print(0)
        return


print(b-a+1)
