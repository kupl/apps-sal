n, k = map(int, input().split())
s = [i == "YES" for i in input().split()]

r = []

name = "Aa"

def nextName():
	nonlocal name
	if name[-1] == 'z': name = name + 'a'
	else: name = name[:-1] + chr(ord(name[-1]) + 1)
	return name

for i in range(k-1):
	r.append(nextName())

for i in range(n-k+1):
	r.append(nextName() if s[i] else r[i])

print(*r)
