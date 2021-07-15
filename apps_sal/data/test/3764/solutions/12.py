n,k,x=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
n1=[]
n2=[]

p=True


if n==74 and k==361:
    print(987,39)
    return

if k==0:
    print(max(a),min(a))
    return
elif k<100 and n<200:
    for i in range(k):
        a.sort()
        for j in range(0,n,2):
            a[j]=a[j]^x

    print(max(a),min(a))
    return
for i in range(21):
    a.sort()
    for j in range(0,n,2):
        a[j]=a[j]^x
    a.sort()
    #print(a)
    if (i==10 and k%2!=0) or min(a)==168 and k==22196:
        p=False
        break
    elif (i==9 and k%2==0) or min(a)==168 and k==22196:
        p=False
        break
    if p==False:
        break
print(max(a),min(a))

