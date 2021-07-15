t, f = list(map(int, input().split()))
s = [f] * 3
count = 0
while sum(s) < 3*t:
	s.sort()
	s[0] = min(t, s[1]+s[2] - 1)
	count += 1
print(count)

