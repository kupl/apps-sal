n = int(input())
x = [int(i) for i in input().split()]
x = sorted(x)
q = int(input())
import bisect
def upperbound(m):
	ind = bisect.bisect(x,m)
	return ind
		

for i in range(q):
	m = int(input())
	print(upperbound(m))
