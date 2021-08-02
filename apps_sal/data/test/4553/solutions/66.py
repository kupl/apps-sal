a, b = map(int, input().split())
s = input()
ans = 'Yes'
for i in range(len(s)):
    if i > a + b:
        ans = 'No'
        break
    if i == a:
        if s[i] != '-':
            ans = 'No'
            break
    elif not s[i].isdigit():
        ans = 'No'
        break
print(ans)
