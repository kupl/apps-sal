n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 1
i = 1
while i < len(a):
	if a[i - 1] > a[i]:
		while i < len(a) and a[i] + k >= a[i - 1]:
			i += 1
	i += 1
	if i - 1 < len(a):
		ans += 1

print(ans)
