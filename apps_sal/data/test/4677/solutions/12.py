s = input()
ans = []
for i in range(len(s)):
    if s[i] == 'B':
        if ans:
            ans.pop()
    else:
        ans.append(s[i])
print((''.join(ans)))
