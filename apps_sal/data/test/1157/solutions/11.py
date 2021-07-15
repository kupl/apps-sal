n=int(input())
a=[int(x) for x in input().split()]
pref=[0]
for item in a:
    if item<0:
        pref.append(pref[-1]+1)
    else:
        pref.append(pref[-1])
non=0
on=0
arr=0
for item in pref:
    if item%2==0:
        arr+=non
        on+=1
    else:
        arr+=on
        non+=1
print(arr,n*(n+1)//2-arr)
    

