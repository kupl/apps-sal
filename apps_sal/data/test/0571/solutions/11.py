n = int(input())
l = list(input())

if n % 2 == 1:
    print(':(')
    return

if n == 2:
    if l[0] == ')' or l[1] == '(':
        print(':(')
    else:
        print('()')
    return

if l[0] == ')' or l[1] == ')' or l[-1] == '(' or l[-2] == '(':
    print(':(')
    return

l[0] = '('
l[1] = '('
l[-1] = ')'
l[-2] = ')'

p = l.count(')') - l.count('(')
q = l.count('?')

a = (q + p) // 2
b = q - a

cnt = 0
for i in range(len(l)):
    if l[i] == '?':
        if cnt < a:
            l[i] = '('
        else:
            l[i] = ')'
        cnt += 1

cnt = 0
for p,i in enumerate(l):
    if i == '(':
        cnt += 1
    else:
        cnt -= 1
    if cnt == 0 and p != n - 1:
        print(':(')
        return
else:
    if cnt != 0:
        print(':(')
        return

print(''.join(l))

