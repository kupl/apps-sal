l = input().split(' ')
H = int(l[0])
W = int(l[1])
K = int(l[2])
c = []
retval = 0
for i in range(H):
  c.append(input())
#print(5&4)
for maski in range((1<<H)):
  for maskj in range((1<<W)):
    count = 0
    #print('maski:'+str(maski))
    #print('maskj:'+str(maskj))
    for i in range(H):
      for j in range(W):
        #print('i: '+str(i)+', j: '+str(j))
        #print('(maski>>i)&1: '+str((maski>>i)&1)+', (maskj>>j)&1: '+str((maskj>>j)&1))
        #if((maski>>i)&1==1) and ((maskj>>j)&1==1):
          #print('i:'+str(i)+',j:'+str(j))
        if((maski>>i)&1==1) and ((maskj>>j)&1==1) and (c[i][j]=='#'):
          count+=1
    #print('##################')
    if(count==K):
      retval+=1
      
print(retval)
