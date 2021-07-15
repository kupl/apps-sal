N=input()
list=[]
t=0
for i in range(len(N)):
    list.append(N[i])
for i in range(len(list)):
    t=t+int(list[i])
if t%9==0:
    print('Yes')
else:
    print('No')
