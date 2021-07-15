a=input().split(' ')
a=[int(i) for i in a]
s=input()
w=[]
for i in s:
    w.append(i)
for _ in range(a[1]):
    q=input().split(' ')
    for i in range(int(q[0])-1,int(q[1])):
        if w[i]==q[2]:
            w[i]=q[3]
for i in w:
    print(i,end='')

