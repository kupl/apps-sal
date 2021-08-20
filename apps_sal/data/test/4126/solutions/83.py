s = input()
ans = 'No'
n = len(s)
if s == s[::-1]:
    tmp = s[0:(n - 1) // 2]
    if tmp == tmp[::-1]:
        tmp = s[(n + 3) // 2 - 1:]
        if tmp == tmp[::-1]:
            ans = 'Yes'
print(ans)
