s = input()
n = len(s)
t = {}
t[s] = True
for i in range(n):
    s = s[1:] + s[0]
    t[s] = True
print(len(t))
