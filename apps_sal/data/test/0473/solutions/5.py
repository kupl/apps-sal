def conv(s):
	h = str(s // 60)
	m = str(s % 60)
	if len(h) < 2:
		h = '0' + h
	if len(m) < 2:
		m = '0' + m
	return h + ':' + m

s = list(map(int, input().split(':')))
t = list(map(int, input().split(':')))
s = s[0] * 60 + s[1]
t = t[0] * 60 + t[1]
p = s - t
if p < 0:
	p += 24 * 60
print(conv(p))

