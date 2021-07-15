n, k = list(map(int, input().split()))
s = input()
def f(x):
	return (ord(x) - ord("a")) + 1
a = []
for i in s:
	a.append(i)
a.sort()
curr = 1
count = 1
ans = 0
last = 0
ans += f(a[0])
while curr < n and count < k:
	if f(a[curr]) - f(a[last]) >= 2:
		ans += f(a[curr])
		last = curr
		count += 1
	curr += 1
if count == k:
	print(ans)
else:
	print(-1)



