s = input()
t = input()
ans = 'No'
for i in range(len(s)):
    a = s[i::] + s[0:i]
    if a == t:
        ans = 'Yes'
print(ans)
