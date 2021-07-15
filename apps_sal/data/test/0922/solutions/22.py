[n,A]=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
tot=0
for x in a:
	tot+=x
for x in a:
	up=min(x,A-(n-1))
	down=max(A-(tot-x),1)
	#print(up,down)
	print(x-(up-down+1),end=" ")
print()
