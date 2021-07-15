import collections
k=int(input().split()[1])
d=[collections.defaultdict(int)for _ in"123"]
for x in map(int,input().split()):
	d[2][k*x]+=d[1][x]
	d[1][k*x]+=d[0][x]
	d[0][k*x]+=1
print(sum(d[2].values()))

