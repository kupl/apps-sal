n=int(input())
sp = [input().split() for _ in range(n)]
orde=sorted(sp,key=lambda sp:(sp[0],-int(sp[1])))
for i in orde:
	print(sp.index(i)+1)
