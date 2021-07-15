n=int(input())
sp=list(map(int,input().split()))
count=1
sont=set()
for x in sp:
    sont^={x}
    if len(sont)>count: count=len(sont)
print(count)
