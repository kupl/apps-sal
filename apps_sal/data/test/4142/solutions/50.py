s = input()
ans = 'Yes'
for i in range(len(s)):
    if (i + 1) % 2 == 1:
        if s[i] == 'L':
            ans = 'No'
    elif s[i] == 'R':
        ans = 'No'
print(ans)
