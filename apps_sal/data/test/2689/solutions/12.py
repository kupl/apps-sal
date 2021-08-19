s = str(input())
# print(len(s))
f = ""
for i in range(len(s)):
    f += s[i]
    if s[i] == '-':
        f += " "
# print(f)
# print(len(f))
g = ""
for i in range(len(f)):
    if f[i].isdigit():
        g += " "
    g += f[i]
# print(g)
# print(len(g))
# print(g.split())
final = ""
e = g.split()
for i in range(len(e)):
    z = e[i]
    # print(z)
    if z[0].isdigit():
        val = z[2:len(z) - 1]
        # print(z[2:len(z)-1])
        final += int(z[0]) * val
    else:
        final += z
# print(final)
if final == final[::-1]:
    print("Return")
else:
    print("Continue")
