n = int(input())
s = input()
ans = 0
for i in range(1, len(s)):
    s1 = s[:i]
    s2 = s[i:]
    cnt = set()
    for j in s1:
        if j in s2:
            cnt.add(j)
    ans = max(ans, len(cnt))
print(ans)
