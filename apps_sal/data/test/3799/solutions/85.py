s = input()
if s[0] == s[-1]:
    if len(s) % 2:
        ans = 'Second'
    else:
        ans = 'First'
elif len(s) % 2:
    ans = 'First'
else:
    ans = 'Second'
print(ans)
