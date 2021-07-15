q=input()
w=input()
l=len(q)
a=[]
s=[0 for i in range(0,130)]
t=[]
for i in range(0,l):
    if q[i]==w[i]:
        t.append(q[i])
for i in range(0,l):
    if q[i]!=w[i]:
        a.append([q[i],w[i]])
        s[ord(q[i])]+=1
        s[ord(w[i])]+=1
        c=q[i]
        if (q[i] in t) | (w[i] in t):
            s[0]=10
        q=q.replace(q[i],w[i])
        w=w.replace(c,w[i])
if max(s)>1:
    print(-1)
else:
    print(len(a))
    for i in a:
        print(i[0],i[1])

