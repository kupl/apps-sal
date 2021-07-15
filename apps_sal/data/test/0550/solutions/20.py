l = input()
new_login1 = l.upper().replace('O', '0').replace('l', '1').replace('I', '1')
new_login2 = l.replace('O', '0').replace('l', '1').replace('I', '1').lower()
new_login3 = l.lower().replace('O', '0').replace('l', '1').replace('I', '1')
logins = []
n = int(input())
for i in range(n):
    last = input()
    logins.append(last.upper().replace('O', '0').replace('l', '1').replace('I', '1'))
    logins.append(last.replace('O', '0').replace('l', '1').replace('I', '1').lower())
    logins.append(last.lower().replace('O', '0').replace('l', '1').replace('I', '1'))
print('No' if new_login1 in logins or new_login2 in logins or new_login3 in logins else 'Yes')

