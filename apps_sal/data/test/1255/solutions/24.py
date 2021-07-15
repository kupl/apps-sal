n = int(input())
ans = 0
last = ''
cur = 0
for i in range(n):
	s = input()
	if s != last:
		last = s
		cur = 0
	cur += 1
	ans = max(ans, cur)
print(max(ans, cur))

