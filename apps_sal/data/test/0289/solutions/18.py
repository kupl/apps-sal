s = input()
k = 0
for i in range(len(s) - 1):
    if s[i] == 'V' and s[i + 1] == 'K':
        k += 1
for i in range(len(s)):
    if i < len(s) - 1:
        if s[i] == 'V' and s[i + 1] == 'V' and i + 2 == len(s):
            k += 1
            break
        if s[i] == 'V' and s[i + 1] == 'V' and s[i + 2] == 'V':
            k += 1
            break
    if i >= 1:
        if i == 1 and s[1] == 'K' and s[0] == 'K':
            k += 1
            break
        if s[i] == 'K' and s[i- 1] == 'K' and s[i - 2] == 'K':
            k += 1
            break
print(k)
