n = int(input())
s = list(input())
for i in range(len(s)):
    s[i] = chr((ord(s[i]) + n - ord('A')) % 26 + ord('A'))
print(''.join(s))
