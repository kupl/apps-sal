n = int(input())
a = list(map(int,input().split()))

codd = 0
cfour = 0

for i in range(n):
	if a[i]%2 != 0:
		codd += 1
	if a[i]%4 == 0:
		cfour += 1
ceven = n - cfour - codd

if cfour >= codd:
	print('Yes')
elif ceven == 0 and cfour + 1 == codd:
	print('Yes')
else:
	print('No')
