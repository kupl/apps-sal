t = list(map(int, input().split(':')))

def isPal(t):
	return t[0] // 10 == t[1] % 10 and t[0] % 10 == t[1] // 10

def next():
	t[1] += 1
	if t[1] == 60:
		t[1] = 0
		t[0] += 1
	if t[0] == 24:
		t[0] = 0

ans = 0
while not isPal(t):
	next()
	ans += 1

print(ans)
