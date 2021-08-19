s = input()
for i in range(len(s)):
    if s[i] == 'A':
        s = s[i:]
        break
for j in range(1, len(s)):
    if s[-j] == 'Z':
        s = s[:-j] + 'Z'
        break
print(len(s))
