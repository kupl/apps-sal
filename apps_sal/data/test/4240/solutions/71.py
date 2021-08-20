s = input()
t = input()
s_temp = s
answer = 'No'
for i in range(len(s)):
    s_temp = s[i:] + s[:i]
    if s_temp == t:
        answer = 'Yes'
        break
print(answer)
