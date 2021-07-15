import math

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res, v1, v2 = 0, 0, 0
for i in range(n):
	if b[i]>1 and b[i]<=2*a[i]:
		v1 = math.ceil(b[i]/2)
		v2 = b[i]-v1
		res += v1*v2
	else:
		res -= 1
print(res)
