s = str(input())
f = ""
for i in range(len(s)):
	f += s[i]
	if s[i] == '-':
		f += " "
g = ""
for i in range(len(f)):
	if f[i].isdigit():
		g += " "
	g += f[i]
final = ""
e = g.split()
for i in range(len(e)):
	z = e[i]
	if z[0].isdigit():
		val = z[2:len(z)-1]
		final += int(z[0])*val
	else:
		final += z
if final == final[::-1]:
	print("Return")
else:
	print("Continue")
