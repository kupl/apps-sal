data=list(input())
c=0
for i in range(0,len(data)-1):
    for j in range(i+1,len(data)):
        if data[i]==data[j]:
            c=c+1
if c==0:
    print('yes')
else:
    print('no')
