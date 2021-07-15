good = set(list(input()))
s = input()
st = '*' in list(s)

def f(x):
	d = len(x) - len(s) + 1
	if d < 0 or (len(x) != len(s) and not st):
		return False
	ind = -1
	for i in range(len(x)):
		if s[i] == '*':
			ind = i
			break
		elif s[i] == '?' and x[i] not in good:
			return False
		elif 'a' <= s[i] <= 'z' and s[i] != x[i]:
			return False

	if ind == -1:
		return True

	for i in range(ind, ind + d):
		if x[i] in good:
			return False

	for i in range(ind + d, len(x)):
		if s[i - d + 1] == '?' and x[i] not in good:
			return False
		elif 'a' <= s[i - d + 1] <= 'z' and s[i - d + 1] != x[i]:
			return False

	return True

n = int(input())
for i in range(n):
	c = input()
	if f(c):
		print("YES")
	else:
		print("NO")
