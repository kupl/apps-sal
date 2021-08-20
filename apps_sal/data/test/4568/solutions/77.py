n = int(input())
s = list(input())
wd = list('abcdefghijklmnopqrstuvwxyz')
ans = 0
for i in range(n):
    s1 = set(s[:i])
    s2 = set(s[i:])
    tmp = 0
    for w in wd:
        if w in s1 and w in s2:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
