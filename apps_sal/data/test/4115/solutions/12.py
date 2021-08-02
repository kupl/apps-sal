s = input()
l = len(s)
ans = 0
for i in range(l // 2):
    if s[i] != s[l - 1 - i]: ans += 1
print(ans)
