s = input()
form = 'nineteen'
ans = 0
flag = True
while True:
    for i in range(len(form)):
        if s.find(form[i]) == -1:
            flag = False
            break
        if i == len(form) - 1:
            ans += 1
        else:
            s = s[:s.find(form[i])] + s[s.find(form[i]) + 1:]
    if not flag:
        break
print(ans)
