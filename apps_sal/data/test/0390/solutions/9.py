
n, a, b = map(int, input().split())

cl = list(map(int, input().split()))
ll = [a, b]

ans = 0
l = 0
r = len(cl) - 1
while l < r:
	if cl[l] == 2 and cl[r] == 2:
		ans += 2 * min(a, b)
	elif cl[l] == 2:
		ans += ll[cl[r]]
	elif cl[r] == 2:
		ans += ll[cl[l]]
	elif cl[l] != cl[r]:
		print(-1)
		return
	l += 1
	r -= 1

if l == r:
	if cl[l] == 2:
		ans += min(a, b)

print(ans)
