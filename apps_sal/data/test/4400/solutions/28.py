s = input()
if s[1] == 'R':
    if s[0] == 'R' and s[2] == 'R':
        ans = 3
    elif s[0] == 'R' or s[2] == 'R':
        ans = 2
    else:
        ans = 1
elif s[0] == 'R' or s[2] == 'R':
    ans = 1
else:
    ans = 0
print(ans)
