s = input()
n = len(s)
ans = 0
i = 0
while i < n:
    if int(s[i]) % 3 == 0:
        ans += 1
        i += 1
        continue
    if i != n - 1 and int(s[i]) % 3 == 1 and int(s[i + 1]) % 3 == 2:
        ans += 1
        i += 2
        continue
    if i != n - 1 and int(s[i]) % 3 == 2 and int(s[i + 1]) % 3 == 1:
        ans += 1
        i += 2
        continue
    if i < n - 2 and int(s[i]) % 3 == int(s[i + 1]) % 3 == int(s[i + 2]) % 3 == 1:
        ans += 1
        i += 3
        continue
    if i < n - 2 and int(s[i]) % 3 == int(s[i + 1]) % 3 == int(s[i + 2]) % 3 == 2:
        ans += 1
        i += 3
        continue
    i += 1

print(ans)

