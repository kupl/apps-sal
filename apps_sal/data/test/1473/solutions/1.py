
n = int(input())
ID = 1000001
thprev = [-1 for i in range(ID)]
thpost = [-1 for i in range(ID)]
prev = []
post = []
for i in range(n):
    a,b = [int(s) for s in input().split()]
    prev.append(a)
    post.append(b)
    thprev[a] = i
    thpost[b] = i
    
sth = thprev[0]
v = post[sth]
q1 = []
while v>0 and sth>=0:      
    q1.append(v)
    sth = thprev[v]
    v = post[sth]

start1 = thprev[0]
for i in range(n):
    if i!=start1 and thpost[prev[i]]==-1:
        start2 = i
        break
    
sth = start2
u = prev[sth]
v = post[sth]
q2 = [u]
while v>0 and sth>=0:      
    q2.append(v)
    sth = thprev[v]
    v = post[sth]


q1.reverse()
q2.reverse()
q = []
label = 2

while q1 or q2:
    if label==1:
        q.append(q1.pop())
        label = 2
    else:
        q.append(q2.pop())
        label = 1
print(' '.join(map(str,q)))
        
    
    
    
    
    
    
    
    

    


