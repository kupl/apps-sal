s = str(input())
t = str(input())
l = len(s)
c = 0
for i in range(l):
    if s[i] != t[i]:
        c += 1
print(c)
