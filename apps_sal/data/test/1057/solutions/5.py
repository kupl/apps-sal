n = int(input())
s = input()
l = 1
while l < n and s[l] == s[l - 1]:
    l += 1
r = 1
while l < n and s[-r - 1] == s[- r]:
    r += 1
ans = 0
if s[0] != s[-1]:
    ans = l + r + 1
elif l == n:
    ans = n * (n + 1) // 2
else:
    ans = (l + 1) * (r + 1)
ans %= 998244353
print(ans)
