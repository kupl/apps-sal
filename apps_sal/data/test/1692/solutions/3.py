s = input()
ans = 0
for i in range(len(s) - 1, -1, -1):
    if int(s[i - 1] + s[i]) % 4 == 0:
        ans += i
    if int(s[i]) % 4 == 0:
        ans += 1
print(ans)
