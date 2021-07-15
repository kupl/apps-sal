s = input()
a = [0]
for i in range(len(s)):
    if s[i] in 'AEIOUY':
        a.append(i + 1)
a.append(len(s) + 1)
ans = 0
for i in range(1, len(a)):
    ans = max(ans, a[i] - a[i - 1])
print(ans)
