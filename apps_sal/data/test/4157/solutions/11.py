n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
mi=min(a)
arr=[mi]
prev=[mi]
while True:
    if (3*prev[-1] in d) and d[3*prev[-1]]>0:
        d[3*prev[-1]]-=1
        prev.append(3*prev[-1])
    elif prev[-1]&1==0 and prev[-1]//2 in d and d[prev[-1]//2]>0:
        d[prev[-1]//2]-=1
        prev.append(prev[-1]//2)
    else:
        break
while True:
    if 2*arr[-1] in d and d[2*arr[-1]]>0:
        d[2*arr[-1]]-=1
        arr.append(2*arr[-1])
    elif arr[-1]%3==0 and arr[-1]//3 in d and d[arr[-1]//3]>0:
        d[arr[-1]//3]-=1
        arr.append(arr[-1]//3)
    else:
        break
#print(prev,arr)
for i in range(len(prev)-1,0,-1):
    print(prev[i],end=" ")
print(*arr)

