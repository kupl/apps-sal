
from bisect import bisect_left

def mi():
	return map(int, input().split())

n = int(input())
a = sorted(list(mi()))

used = [0]*n
ma = 2*(10**9)
for i in range(n):
	t = 1
	if used[i]==1:
		continue
	while t<a[i]:
		t*=2
	target = t-a[i]
	while target<ma:
		found=0
		i1 = bisect_left(a, target)
		if i1 != n and a[i1] == target:
			while i1<n and  a[i1]==target:
				if a[i1]==target and i1!=i:
					used[i] = 1
					used[i1] = 1
					found=1
					break
				else:
					i1+=1
		t*=2
		target = t-a[i]
		if found:
			break
print(used.count(0))
