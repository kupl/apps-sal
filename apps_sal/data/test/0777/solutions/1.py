s = input()
n = len(s)
ss = set()
a = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n + 1):
    for j in range(26):
        ss.add(s[:i] + a[j] + s[i:])
print(len(ss))
