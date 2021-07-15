q,w=input().split()
s=q[0]
q=q[1:]
while len(q)>0:
    if q[0]<w[0]:
        s+=q[0]
        q=q[1:]
    else:
        q=''
print(s+w[0])

