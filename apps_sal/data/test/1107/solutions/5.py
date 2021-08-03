cnt, n, ans = 1, int(input()), 0
s = input()
for i in range(1, len(s)):
    if cnt == 0 and s[i - 1] == s[i - 2] == s[i - 3]:
        ans += 1
    cnt += 1
    if cnt == n:
        cnt = 0
print(ans)
