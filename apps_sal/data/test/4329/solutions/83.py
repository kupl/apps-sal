s = input()
t = input()
ans = 'No'
if len(s) + 1 == len(t):
    for i in range(len(s)):
        if s[i] != t[i]:
            break
        if i == len(s) - 1:
            ans = 'Yes'
print(ans)
