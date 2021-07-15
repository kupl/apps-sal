n=int(input())
s=input().split()
mx=0
for c in s:
    tot=0
    for x in c:
        if x==x.upper():
            tot+=1
    mx=max(mx,tot)
print(mx)
