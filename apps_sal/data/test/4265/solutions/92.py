s = list(map(str, input()))
t = list(map(str, input()))

ans = 0

for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)
