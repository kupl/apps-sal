s = input()
odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']
ans = 'Yes'
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] not in odd:
            ans = 'No'
    elif s[i] not in even:
        ans = 'No'
print(ans)
