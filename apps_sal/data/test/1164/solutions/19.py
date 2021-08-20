s = input()
c = set()
c.add('1')
c.add('2')
c.add('3')
c.add('4')
c.add('5')
c.add('6')
c.add('7')
c.add('8')
c.add('9')
c.add('0')
c.add('.')
ans = []
j = 0
st = ''
for i in range(len(s)):
    if s[i] in c:
        st += s[i]
    elif len(st) > 0:
        ans.append(st)
        st = ''
x = 0
ans.append(st)
for i in range(len(ans)):
    if len(ans[i]) < 3:
        ans[i] += '.00'
    if ans[i][-3] != '.':
        ans[i] += '.00'
cc = set()
cc.add('1')
cc.add('2')
cc.add('3')
cc.add('4')
cc.add('5')
cc.add('6')
cc.add('7')
cc.add('8')
cc.add('9')
cc.add('0')
pp = ''
pk = 0
pr = 0
for i in range(len(ans)):
    for j in range(len(ans[i]) - 1, -1, -1):
        if ans[i][j] == '.':
            x = j
            break
    p1 = ans[i][:x]
    p2 = ans[i][x + 1:]
    for ii in range(len(p1)):
        if p1[ii] in cc:
            pp += p1[ii]
    pr += int(pp)
    pp = ''
    pk += int(p2)
while pk > 99:
    pk -= 100
    pr += 1
pk = str(pk)
if len(pk) < 2:
    pk = '0' + pk
answer = str(pr) + '.' + pk
j = answer.index('.')
q = 0
for i in range(j, -1, -1):
    if q == 2:
        answer = answer[:i] + '.' + answer[i:]
        q = 0
    elif answer[i] != '.':
        q += 1
if answer[-1] == '0' and answer[-2] == '0' and (answer[-3] == '.'):
    answer = answer[:-3]
if answer[0] == '.':
    answer = answer[1:]
print(answer)
"\n        ans[j] = ans[j] * 10 + int(s[i])\n    elif s[i] == '.':\n        ans[j] *= 100"
