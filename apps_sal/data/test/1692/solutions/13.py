s = input()
ans = 0
i = len(s) - 1
while i != -1:
    if i == 0:
        if int(s[i]) % 4 == 0:
            ans += 1
    else:
        if int(s[i - 1] + s[i]) % 4 == 0:
            ans += i
        if int(s[i]) % 4 == 0:
            ans += 1
    i -= 1
print(ans)
