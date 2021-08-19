import string


def f():
    return input()


n = int(f())
s = f().lower()
ret = True
for c in string.ascii_lowercase:
    if not c in s:
        ret = False
        break
if ret:
    print('YES')
else:
    print('NO')
