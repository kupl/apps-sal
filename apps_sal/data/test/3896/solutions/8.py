s, m, ans = input()[::-1], int(1e9 + 7), 0
for i in range(len(s)):
    ans *= 2
    if s[i] == '1':
        ans += pow(2, 2 * i, m)
    ans %= m
print(ans)
