s=input()
L=[s[i] for i in range(len(s))]
A=[]
ListOfSum=[0]
for i in range(len(L)-1):
    if L[i]==L[i+1]: ListOfSum.append(ListOfSum[i]+1)
    else: ListOfSum.append(ListOfSum[i])
m=int(input())
for i in range(m):
    Z=[int(t) for t in input().split()]
    A.append(ListOfSum[Z[1]-1]-ListOfSum[Z[0]-1])
for i in range(m): print(A[i])
