sa=input().split(' ')
songs=int(sa[0])
mins=int(sa[1])
sa2=input().split(' ')
sa3=[]
for item in sa2:
    sa3.append(int(item))

sums=0
for item in sa3:
    sums+=item
    
if (songs-1)*10+sums>mins:
    print(-1)

else:
    print((mins-sums)//(5))

