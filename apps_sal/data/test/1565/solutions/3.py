n = int(input())
s = input()
ans = 10**(10**5 + 1)
i = n // 2 + 1
while i < n and s[i] == '0':
    i += 1
if i < n:
    ans = min(ans, int(s[:i]) + int(s[i:]))
i = n // 2
while s[i] == '0':
    i -= 1
if i > 0:
    ans = min(ans, int(s[:i]) + int(s[i:]))
print(ans)
