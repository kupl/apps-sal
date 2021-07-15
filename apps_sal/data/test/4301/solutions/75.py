N=int(input())
a=[int(input()) for i in range(N)]
sw=True
b=sorted(a,reverse=True)

if b[0]>b[1]:
    max2=b[1]
    max1=b[0]
    sw=False

if sw==True:
    max1=b[0]
    for k in range(N):
        print(max1)
else:
    for k in range(N):
        if a[k]==max1:
            print(max2)
        else:
            print(max1)

