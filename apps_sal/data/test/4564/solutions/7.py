s = input()
l = []
for i in range(len(s)):
    if not s[i] in l:
        l.append(s[i])
    else :
        print('no')
        return
print('yes')


