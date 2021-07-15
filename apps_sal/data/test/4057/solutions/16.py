import collections
n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
mxm = 0
for i in c:
	if c[i] > mxm:
		mxm = c[i]
print(mxm)
