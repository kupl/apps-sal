n=int(input())
st=[int(i) for i in input().split()]
et=[int(i) for i in input().split()]
temp=et[0]
t=[0]
for i in range(1,n):
    if st[i]>=temp:
        #print(st[i],temp)
        temp=et[i]
        t.append(i)
for i in range(len(t)):
    print(t[i],end=" ")
