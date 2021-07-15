import string

names = {c: 0 for c in string.ascii_lowercase}

for _ in range(int(input())):
	names[input()[0]] += 1

c = 0

f = lambda n: n * (n - 1) // 2

for k in names:
	c += f(names[k] // 2) + f(-(-names[k] // 2))

print(c)
