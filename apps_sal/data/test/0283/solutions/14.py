n=int(input())

flag=True

m=1
a=[True]*1000001
a[1]=False

for i in range(2,len(a)):
    if a[i]:
        for j in range(2*i,len(a),i):
            a[j]=False

while flag:
    if a[m*n+1]==False:
        flag=False
        print(m)
    else:
        m+=1

