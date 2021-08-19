(s, m, ans) = (input()[::-1], int(1000000000.0 + 7), 0)
for i in range(len(s)):
    if s[i] == '1':
        ans = (ans + pow(2, i, m)) % m
print(ans * pow(2, len(s) - 1, m) % m)
