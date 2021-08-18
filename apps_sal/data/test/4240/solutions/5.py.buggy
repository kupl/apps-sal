import sys
s = input()
t = input()

s = list(s)
t = list(t)
u = s[:]

for i in range(len(s)):
    u.append(s[i])
    u.remove(u[0])
    if u == t:
        print('Yes')
        return
print('No')
