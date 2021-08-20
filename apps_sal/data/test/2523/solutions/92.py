s = input()
l = len(s)
ans = 1000000000000
for i in range(l - 1):
    if s[i] != s[i + 1]:
        ne = max(i + 1, l - i - 1)
        ans = min(ans, ne)
if ans == 1000000000000:
    print(l)
else:
    print(ans)
