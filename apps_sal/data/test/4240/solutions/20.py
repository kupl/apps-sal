s = input()
t = input()
temp = s
ans = 'No'
for i in range(len(s)):
    temp = temp[-1] + temp[:-1]
    if temp == t:
        ans = 'Yes'
        break
print(ans)
