s = input()
n = len(s)
if n == 1:
    t = s
else:
    t = s[0] + s[1]
i = 2
j = 1
while i < n:
    if s[i] == t[j] and s[i] == t[j - 1]:
        i += 1
        continue
    elif s[i] == t[j] and j > 1 and (t[j - 1] == t[j - 2]):
        i += 1
        continue
    else:
        t += s[i]
        i += 1
        j += 1
print(t)
