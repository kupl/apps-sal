n,m=map(int,input().split())
l=[]
l=list(map(int,input().split()))
a=[-1]*(n+1)
s=set()
sorry = False
for i in range(1,n+1):
    s.add(i)
for i in range(m-1):
    temp = (l[i+1] + n - l[i])%n
    if(temp == 0):
        temp = n
    #print(temp)
    if(a[l[i]] == -1 and temp in s):
        a[l[i]] = temp
        s.remove(temp)

    elif(a[l[i]] == temp):
        continue
    else:
        sorry=True
        break

if(sorry):
    print(-1)
else:
    ss = list(s)
    x=0
    for i in range(1,len(a)):
        if(a[i] == -1):
            a[i] = ss[x]
            x+=1
        print(a[i],"",end='')

