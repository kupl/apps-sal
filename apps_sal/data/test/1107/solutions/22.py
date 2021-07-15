n = int(input())
s = str(input())

sl = len(s)
d = 0

for i in range(n, sl, n):
    if s[i-1] == s[i-2] and s[i-1] == s[i-3]:
        d += 1

print(d)

