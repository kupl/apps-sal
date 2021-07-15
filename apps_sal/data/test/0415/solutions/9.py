n = int(input())
a = list(map(int, input().split()))
pref = [0] * (n + 1)

for i in range(1, n + 1):
	pref[i] = pref[i - 1] + a[i - 1]

res = 0
for l in range(1, n + 1):
	for r in range(l, n + 1):
		if (pref[r] - pref[l - 1] > 100 * (r - l + 1)):
			res = max(res, r - l + 1)

print(res)
