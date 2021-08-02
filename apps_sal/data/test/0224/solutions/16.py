s = input()
last = -1
ans = -1
for i in range(len(s)):
    if s[i] in 'AEIOUY':
        ans = max(ans, i - last)
        last = i
ans = max(ans, len(s) - last)
print(ans)
