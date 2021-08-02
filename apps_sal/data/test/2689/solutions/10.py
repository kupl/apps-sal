s = str(input())
f = ""
for i in range(len(s)):
    f += s[i]
    if s[i] == '-': f += " "
g = ""
for i in range(len(f)):
    if f[i].isdigit(): g += " "
    g += f[i]
final = ""
e = g.split()
for i in range(len(e)): z = e[i]; final = (final + int(z[0]) * (z[2:len(z) - 1]) if z[0].isdigit() else final + z)
print("Return") if final == final[::-1] else print("Continue")
