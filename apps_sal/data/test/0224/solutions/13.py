s = input()
s = 'A' + s
s += 'A'
gl = ['A', 'E', 'I', 'O', 'U', 'Y']
a = []
for i in range(len(s)):
    if s[i] in gl:
        a.append(i)
ans = -1
for i in range(1, len(a)):
    ans = max(ans, a[i] - a[i - 1])
print(ans)

