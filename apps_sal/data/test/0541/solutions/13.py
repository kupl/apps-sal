_,*l = [list(map(int,i.split())) for i in open(0)]
l.sort(key=lambda x:x[1])
A=S=0
for s,t in l:
    if S<=s:
        A+=1
        S=t
print(A)
