ss = 'aeiou13579'

s = input()

ans = 0

for c in s:
	if c in ss:
		ans += 1

print(ans)
