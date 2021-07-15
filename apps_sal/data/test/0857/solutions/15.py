a=[int(q) for q in input().strip().split()]
b=[int(q) for q in input().strip().split()]
c=[int(q) for q in input().strip().split()]
d=[]
for k in range(len(b)):
    if b[k]in c:
        d.append(str(b[k]))
print(' '.join(d))
