s = input()
ans = 'Yes'
for i in range(len(s)):
    if (i+1) % 2 == 1:
        if s[i] not in ['R', 'U', 'D']:
            ans = 'No'
            break
    else:
        if s[i] not in ['L', 'U', 'D']:
            ans = 'No'
            break
print(ans)
