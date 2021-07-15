n = int(input())
a = [int(x) for x in input().split()]
s = sum(a)
if s % 3:
	print(0)
	return
cur = 0
cnt = 0
s //= 3
ans = 0
for x in a:
	cur += x
	if s == 0:
		if cur == 0:
			cnt += 1
		continue
	if cur == s:
		cnt += 1
	if cur == s * 2:
		ans += cnt
if s == 0:
	print((cnt - 1) * (cnt - 2) // 2)
else:
	print(ans)

