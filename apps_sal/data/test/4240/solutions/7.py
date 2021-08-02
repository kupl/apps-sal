s = input()
t = input()

ans = 'No'
for _ in range(len(s)):
    s = s[-1] + s[0: len(s) - 1]
    if s == t:
        ans = 'Yes'
        break
print(ans)
