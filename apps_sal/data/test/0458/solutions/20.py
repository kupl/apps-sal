a,b,c= list(map(int,input().split()))

count = 0
arr=[]
def s(x):
    m = str(x)
    k = 0
    for i in m:
        k+=int(i)
    return k
for y in range(1,82):
    p = (b*pow(y,a)+c)
    if p>0 and p<(10**9):
        if s(p)==y:

            count+=1
            arr.append(p)
            #print(p)
print(count)
for x in arr:
    print(x,end=" ")



