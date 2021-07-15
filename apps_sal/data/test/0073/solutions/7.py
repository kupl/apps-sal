c, v0, v1, a, l = map(int, input().split())

ans = 0
while c > 0:
	if ans: c += l
	c -= min(v0, v1)
	v0 += a
	ans += 1
print(ans)
