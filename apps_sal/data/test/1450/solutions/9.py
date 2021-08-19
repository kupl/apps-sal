s = input()
t = ''
num = 0
for i in range(len(s)):
    if s[i] == '1':
        num += 1
    else:
        t += s[i]
s = num * '1' + t
p = s.split('0')
q = []
for k in p:
    q.append(''.join(sorted(list(k))))
p = '0'.join(q)
p = p.split('2')
q = []
for k in p:
    q.append(''.join(sorted(list(k))))
p = '2'.join(q)
print(p)
