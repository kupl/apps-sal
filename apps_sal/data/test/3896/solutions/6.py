mod = int(1000000000.0 + 7)
s = input()
s = s[::-1]
ans = 0
for i in range(len(s)):
    ans *= 2
    if s[i] == '1':
        ans += pow(2, 2 * i, mod)
    ans %= mod
print(ans)
