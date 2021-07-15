n = int(input())
a=[int(_) for _ in input().strip().split()]

mini=min(a)
a=[_-mini for _ in a]
pos = mini%n
count = 0
while True:
	if a[pos] - count <=0:
		print(pos+1)
		break
	else:
		count+=1
		pos=(pos+1)%n
