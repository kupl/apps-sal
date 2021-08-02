s = 'A' + input() + 'A'
a = 'AEIOUY'
ans = 0
last = 0
for i in range(len(s)):
    if s[i] in a:
        ans = max(ans, i - last)
        last = i
print(ans)
