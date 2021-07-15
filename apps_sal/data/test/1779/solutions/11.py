s1 = input()
s2 = input()
t = input()
d = {}
for i in range(len(s1)):
	d[s1[i]] = s2[i]
	d[s1[i].upper()] = s2[i].upper()

for i in range(10):
	d[str(i)] = str(i)

ans = ''
for i in range(len(t)):
	ans += d[t[i]]
print(ans)
