s = input(); ans = 0
for i in range(0, len(s)):
    if s[i] == '1':
        ans += 10
    elif s[i] == 'A':
        ans += 1
    else:
        ans += int(s[i])
print(ans)
