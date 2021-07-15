n=int(input())
a={}
for i in range(n):
    q=input().split()
    if q[0] in a:
        a[q[0]]+=q[2:]
    else:
        a[q[0]]=q[2:]
print(len(a))
for w in a:
    b=a[w]
    b.sort(key=lambda x:len(x))
    i=0
    while True:
        j=i+0
        while j!=len(b)-1:
            j+=1
            if b[i] == b[j][len(b[j])-len(b[i]):]:
                del b[i]
                break
        else:
            i+=1
        if i==len(b):
            break
    print(w,len(b),*b)


