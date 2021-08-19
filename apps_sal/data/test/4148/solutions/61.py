n = int(input())
s = list(input())
ans = []
for i in range(len(s)):
    a = int((ord(s[i]) + n) % 65 % 26)
    ans.append(chr(a + 65))
print(''.join(ans))
