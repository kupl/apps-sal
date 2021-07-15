s = input()
q = 0
w = 0
for i in range(1, len(s)):
    if (s[i] == '0'):
        q *= 10
    w += q
    q = int(s[i])
w += q
print(w + 1)
