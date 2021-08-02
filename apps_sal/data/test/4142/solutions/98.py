s = input()

odds = ['R', 'U', 'D']
evens = ['L', 'U', 'D']

for i in range(len(s)):
    if i % 2 != 0:
        if s[i] not in evens:
            ans = 'No'
            break
    else:
        if s[i] not in odds:
            ans = 'No'
            break
else:
    ans = 'Yes'

print(ans)
