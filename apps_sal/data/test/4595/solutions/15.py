s = input()
n = len(s)
t = []
for i in range(n):
    t.append(s[n - 1 - i])
a = s.index('A')
z = t.index('Z')
print(n - z - a)
