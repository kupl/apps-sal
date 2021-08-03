n = int(input())
s = input()
if (n > 26):
    print(-1)
else:
    d = dict()
    for i in range(len(s)):
        d[s[i]] = d.get(s[i], 0) + 1
    ans = 0
    for i in d:
        ans += d[i] - 1
    print(ans)
