s = input()
t = input()
n = len(s)
a = 0

for i in range(n):
    if s[i] != t[i]:
        a += 1

print(a)
