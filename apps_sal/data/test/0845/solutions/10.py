qwerty = 'qwertyuiopasdfghjkl;zxcvbnm,./'
ans = []
if input() == 'R':
    r = True
else:
    r = False
a = input()
if r:
    for item in a:
        ans += [qwerty[qwerty.find(item) - 1]]
else:
    for item in a:
        ans += [qwerty[qwerty.find(item) + 1]]
print(''.join(ans))
