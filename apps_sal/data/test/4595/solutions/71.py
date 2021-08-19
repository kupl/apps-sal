s = input()
(a, z) = (len(s), 0)
for i in range(len(s)):
    if s[i] == 'A':
        a = min(i, a)
    elif s[i] == 'Z':
        z = max(i, z)
print(z - a + 1)
