s = list(reversed(input()))
t = list(reversed(input()))
i = 0
while i < len(s) and i < len(t) and s[i] == t[i]:
    i += 1
print(len(s) - i + len(t) - i)
