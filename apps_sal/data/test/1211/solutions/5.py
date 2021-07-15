l = list(map(int,input().split()))
n = l[0]
k = l[1]
a = list(map(int,input().split()))
mx = 0
midx = 0
for i in range(k):
	if a[i]*(n // a[i]) > mx:
		mx = a[i]*(n // a[i])
		midx = i
print(midx+1,n // a[midx])
