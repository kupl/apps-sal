_,*li = [list(map(int,i.split())) for i in open(0)]
li.sort(key=lambda x:x[1])
A = 0
S = 0
for s,t in li:
    if S<=s:
        A+=1
        S=t
print(A)
