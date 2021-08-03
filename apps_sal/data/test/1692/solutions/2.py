s = input()
n = len(s)
ans = 0
for i in range(1, n):
    if (int(s[i - 1]) * 10 + int(s[i])) % 4 == 0:
        ans += i
for i in range(n):
    if int(s[i]) % 4 == 0:
        ans += 1
print(ans)
