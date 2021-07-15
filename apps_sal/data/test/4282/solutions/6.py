import sys
n=int(sys.stdin.readline())
l=[]
dct={}
for i in range(n):
    x=list(map(int,sys.stdin.readline().split()))
    dct[str(x)]=0
    l.append(x)
this=1
nxt=-1
nxt2nxt=-1
x,y=l[0][0],l[0][1]
if str([1,y]) in dct or str([y,1]) in dct:
    nxt=y
    nxt2nxt=x
else:
    nxt=x
    nxt2nxt=y
for i in range(n):
    sys.stdout.write(str(this)+" ")
    this=nxt
    nxt=nxt2nxt
    if(l[this-1][0]==nxt):
        nxt2nxt=l[this-1][1]
    else:
        nxt2nxt=l[this-1][0]
