s = input()
t = input()
s = sorted(s)
t = sorted(t)[::-1]
answer = 'Yes'
for i in range(len(s)):
    if i == len(t):
        answer = 'No'
        break
    s_c = s[i]
    t_c = t[i]
    if s_c < t_c:
        break
    elif s_c == t_c:
        continue
    else:
        answer = 'No'
        break
if s == t:
    answer = 'No'
print(answer)
