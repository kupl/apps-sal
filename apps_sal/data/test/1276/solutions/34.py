n = int(input())
s = input()
ans = s.count('R') * s.count('G') * s.count('B')
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if 2 * j - i > n - 1:
            break
        if s[i] != s[j] and s[j] != s[2 * j - i] and (s[i] != s[2 * j - i]):
            ans -= 1
print(ans)
