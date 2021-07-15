n=int(input())
a=list(map(int,input().split()))
b=set()
for i in a:
	while i in b:
		b.remove(i)
		i+=1
	b.add(i)
print(max(b)-len(b)+1)
