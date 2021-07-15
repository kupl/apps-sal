l=list(map(int,input().split()))
l.sort()
if l[2]>=l[0]+l[1]:
    print(l[2]+1-l[0]-l[1])
else:
    print(0)
