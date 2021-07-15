input()
sp=input().split()
count=1
sont=set()
for x in sp:
	sont^={x}
	l = len(sont)
	if l>count: count=l
print(count)

