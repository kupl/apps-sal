n=int(input())
def find(x,d=[]):
    if x==0 and d!=[]:
        return True
    l=x%10
    
    i=-1
    a=False
    for lis in s:
        i+=1
        if l in lis and i not in d:
            a=max(a,find(x//10,d+[i]))
    return a
s=[list(map(int,input().split())) for x in range(n)]
e=1
while find(e):
    e+=1
print(int(e-1  if find(1) else 0))
