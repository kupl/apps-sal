len = int(input())
s = input()
ans = int(s)
for i in range((len - 1) // 2, 0, -1):
    if s[i] != '0':
        ans = min(ans, int(s[:i]) + int(s[i:]))
        break
for i in range(len // 2 + 1, len):
    if s[i] != '0':
        ans = min(ans, int(s[:i]) + int(s[i:]))
        break
if len % 2 == 0 and s[len // 2] != '0':
    i = len // 2
    ans = min(ans, int(s[:i]) + int(s[i:]))
print(ans)
