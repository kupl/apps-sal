(n, k) = map(int, input().split())
s = input()
ans = 0
for (i, j) in zip(s[:-1], s[1:]):
    if i + j == 'LL' or i + j == 'RR':
        ans += 1
print(min(n - 1, ans + 2 * k))
