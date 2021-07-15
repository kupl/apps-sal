s = input()
ans = 0
for i in range(0, len(s) - 1):
    if int(s[i:i + 2]) % 4 == 0:
        ans += i + 1
    if int(s[i]) % 4 == 0:
        ans += 1
if int(s[len(s) - 1]) % 4 == 0:
    ans += 1
print(ans)

