n=int(input())
s=input()
cur=0
for a in s:
    cur=max(cur,0)
    if(a=='-'):
        cur-=1
    else: cur+=1
    cur=max(cur,0)
print(cur)
