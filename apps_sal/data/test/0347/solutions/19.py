sc=[1]*10
mrk=input().split()
for i in range (0,5):
    mrk[i]=int(mrk[i])
    sc[i]=500*(i+1)
wr=input().split()
for i in range (0,5):
    wr[i]=int(wr[i])
s=0
for i in range (0,5):
    s+=max((0.3*sc[i]),(1-(mrk[i]/250))*sc[i]-(50*wr[i]))
l=input().split()
s+=100*int(l[0])-50*int(l[1])
print(int(s))


