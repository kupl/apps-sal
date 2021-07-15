s = input()
ans = 0
for i in s:
    if int(i) % 4 == 0:
        ans += 1
for i in range(len(s) - 1):
    if int(s[i:i + 2]) % 4 == 0:
        ans += i + 1
print(ans)

