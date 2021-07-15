def need_check(c):
	if c in ['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7', '9']:
		return True
	return False

s = str(input())
tot = 0
for c in s:
	if need_check(c):
		tot = tot + 1
print(tot)
