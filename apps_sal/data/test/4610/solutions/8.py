import operator
n,k=[int(_) for _ in input().split()]
D=dict()
A=[int(_) for _ in input().split()]
for _ in range(n):
    if A[_] in D:
        D[A[_]]+=1
    else:
        D[A[_]]=1
D=dict(sorted(list(D.items()), key=operator.itemgetter(1),reverse=True))
c=0
i=0
for _ in D:
    if i>=k:
        c+=D[_]
    i+=1
print(c)

