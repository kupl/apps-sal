n= int(input())
a= list(map(int,input().split()))
adict = {}
for c in a:adict[c] = adict.get(c,0) + 1
twos=0
moreodd=0
moreeven=0
for num in adict.keys():
    if adict[num]==2:twos+=1
    elif adict[num]>2:
        if adict[num]%2==0:moreeven+=1
        else:moreodd +=1
if moreeven%2==1:twos+=1
if twos%2==0:print(len(adict))
else:print(len(adict)-1)
