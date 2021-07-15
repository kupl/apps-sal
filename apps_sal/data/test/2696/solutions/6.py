def checklist(a):
	return len(set(a)) == 1

n =int(input())
a =list(map(int, input().split()))
x=0
if checklist(a) == True:
	x=1
	print(1)
elif x==0:	
	while a[n-1] == a[n-2]:
		n-=1
	print(n)
