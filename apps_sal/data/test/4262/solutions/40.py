import itertools
n=int(int(input()))
a=[i+1 for i in range(n)]
p=tuple(map(int,input().split()))
q=tuple(map(int,input().split()))
c=0
d=0
e=0
for i in itertools.permutations(a,n):
    c+=1
    if p==i:
        d=c
    if q==i:
        e=c
print(abs(d-e))
