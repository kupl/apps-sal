s = input()
a = [-1]
for i in range(len(s)):
    if s[i] in ['A', 'E', 'I', 'O', 'U', 'Y']:
        a += [i]
a += [len(s)]
ans = -1
for i in range(1, len(a)):
    ans = max(ans, a[i] - a[i - 1])
print(ans)
