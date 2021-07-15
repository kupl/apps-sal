n, k = [int(x) for x in input().split()]
l = [x for x in input().split()]
ans = 0
for x in l:
	if x.count('4') + x.count('7') <= k:
		ans += 1
print(ans)

