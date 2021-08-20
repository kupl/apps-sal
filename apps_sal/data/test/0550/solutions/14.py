def unify_login(login):
    login = login.lower()
    login = login.replace('0', 'o')
    login = login.replace('l', '1')
    login = login.replace('i', '1')
    return login


s = unify_login(input())
n = int(input())
logins = set()
for i in range(n):
    logins.add(unify_login(input()))
if s in logins:
    print('No')
else:
    print('Yes')
