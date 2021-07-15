s = input()
temp = None
paste = None
zero, one = 0,0
for i in range(len(s)):
    if s[i] == '2':
        temp = s[i:]
        break
    elif s[i] == '1':
        one += 1
    elif s[i] == '0':
        zero += 1
if temp is not None:
    for x in temp:
        if x == '1':
            one += 1
    paste = temp.replace("1", "")
ans = '0'*zero + '1'*one
if paste is not None:
    ans += paste
print(ans)

