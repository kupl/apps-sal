s = [int(x) for x in input()]
ans = 0
if s[0] % 4 == 0:
    ans += 1
for i in range(1, len(s)):
    if s[i] % 4 == 0:
        ans += 1
    if (s[i] + 10 * s[i - 1]) % 4 == 0:
        ans += i
print(ans)
