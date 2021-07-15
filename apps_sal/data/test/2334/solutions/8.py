def g(q, x, f, a):
	if(((a + q - 1) // q) - ((q - 1) * f) <= x):
		return True
	else:
		return False

s = input()
n = int(s)


s = input()
y = s.split()

s = input()
s = s.split()

x = int(s[0])
f = int(s[1])

ans = 0

for i in y:
	ans += (int(i) + f - 1) // (x + f)

print(ans * f)


