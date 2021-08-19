s = input()
o = ['R', 'U', 'D']
e = ['L', 'U', 'D']
ans = 'Yes'
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] not in o:
            ans = 'No'
    elif s[i] not in e:
        ans = 'No'
print(ans)
