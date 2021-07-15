s = input()
if s[0] !='A':
    print('WA')
    return
if 'C' not in s[2:len(s)-1]:
    print('WA')
    return
cnt = 0
for i in s:
    if i.isupper():
        cnt +=1
if cnt !=2:
    print('WA')
    return
print('AC')

