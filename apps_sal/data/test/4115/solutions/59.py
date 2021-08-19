s = input()
s = ' ' + s
ans = 0
if len(s) % 2 == 0:
    for i in range(1, len(s) // 2 + 1):
        if s[i] != s[i * -1]:
            ans += 1
else:
    for i in range(1, len(s) // 2 + 1):
        if s[i] != s[i * -1]:
            ans += 1
print(ans)
