n = int(input())
s = input()
ans = 0
k1, k2 = 0, -1
for i in range(1, n):
    if s[i] != s[0]:
        k1 = i
        break
for i in range(n - 2, -1, -1):
    if s[i] != s[-1]:
        k2 = i
        break
if s[0] == s[-1]:
    ans = (k1 + 1) * (n - k2)
else:
    ans += k1 + n - k2 - 1
    ans += 1
print(ans % 998244353)
