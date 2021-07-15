def getCoord(x, y, t):
	if t == 'U':
		return (x, y + 1)
	return (x + 1, y)

n = int(input())
s = input()
x, y = getCoord(0, 0, s[0])
t = 1
if x < y:
	t = 0
ans = 0
for ch in s[1:]:
	x, y = getCoord(x, y, ch)
	if x == y:
		continue
	nt = 1
	if x < y:
		nt = 0
	if t != nt:
		t = nt
		ans += 1
print(ans)
