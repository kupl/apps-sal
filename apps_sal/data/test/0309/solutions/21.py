import sys
l,r=list(map(int,sys.stdin.readline().split()))
binr=list(str(bin(r)))[2:]
binl=list(str(bin(l)))[2:]
lenr=len(binr)
lenl=len(binl)
for i in range(lenr-lenl):
    binl.insert(0,0)

ans=['1']
length=lenr
status=0
for i in range(0,length):
    if status==1:
        ans.append('1')
    if(binr[i]!=binl[i]):
        status=1

if(status==0):
    print(0)
else:
    strans=''.join(ans)
    print(int(strans,2))

        


