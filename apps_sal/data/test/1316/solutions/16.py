n, k = map(int, input().split())
s = input()+'.'
a = [1 for i in range(n)]
d = {}

for i in range(1, n):
    if s[i] == s[i-1]:
        a[i] = a[i-1]+1
for i in range(n):
    if s[i] != s[i+1]:
        if s[i] in d:
            if a[i] in d[s[i]]:
                d[s[i]][a[i]] += 1
            else:
                d[s[i]][a[i]] = 1
        else:
            d[s[i]] = {}
            d[s[i]][a[i]] = 1
ans = 0
for c in d:
    tmpa = 0
    for size in d[c]:
        if size >= k:
            tmpa += (size//k)*d[c][size]
    ans = max(ans, tmpa)
print(ans)
