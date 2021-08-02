s = input()
for i in range(len(s)):
    if s[i] == 'A':
        p = i
        break
for i in range(1, len(s) + 1):
    if s[-i] == 'Z':
        q = i - 1
        break
print(len(s) - (p + q))
