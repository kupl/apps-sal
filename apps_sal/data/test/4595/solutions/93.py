s = str(input())
a = len(s)
z = 0
for i in range(len(s)):
    if s[i] == 'A':
        a = min(a, i)
    if s[i] == 'Z':
        z = max(z, i)

print((z - a + 1))
