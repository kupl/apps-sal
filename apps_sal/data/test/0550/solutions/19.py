def change(s):
    s = s.lower()
    s = s.replace('o', '0')
    s = s.replace('l', '1')
    s = s.replace('i', '1')
    return s

log = change(input())

num = int(input())
logins = []
for i in range(0, num):
    logins.append(change(input()))

if log in logins:
    print('No')
else:
    print('Yes')

