n = int(input())
s = list(input())
for i in range(len(s)):
    s[i] = chr((ord(s[i]) - 65 + n) % 26 + 65)
print(''.join(s))
