'''input
cab
'''
s = input()
m = ["z"] * len(s)
m[-1] = s[-1]
c = s[-1]
for x in range(len(s) - 2, -1, -1):
    c = min(c, s[x])
    m[x] = c
i = m.index(min(m))
t = []
y = ""
for x in range(len(s)):
    while t and t[-1] <= m[x]:
        y += t.pop()
    t.append(s[x])
print(y, end="")
for x in t[::-1]:
    print(x, end="")
# s1 = sorted(s)
# t, u = [], []
# for l in s1:
# 	if l in s:
# 		i = s.index(l)
# 		t += s[:i]
# 		del s[:i+1]
# 		u.append(l)
# print("".join(u + t[::-1]))
