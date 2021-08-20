n = int(input())
tg = False
st = ''
for i in range(n):
    s = input()
    if 'OO' in s and (not tg):
        tg = True
        if s == 'OO|OO':
            s = '++|OO'
        else:
            s = s.replace('OO', '++')
    st += s + '\n'
print('YES' if tg else 'NO')
if tg:
    print(st)
