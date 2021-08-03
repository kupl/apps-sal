n = int(input().strip())
s = input().strip()
ans = 0
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        ans += i + 1
print(ans)
