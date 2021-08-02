sa = input()
sb = input()
sc = input()
s = []
s.append(sa.replace('a', '0').replace('b', '1').replace('c', '2'))
s.append(sb.replace('a', '0').replace('b', '1').replace('c', '2'))
s.append(sc.replace('a', '0').replace('b', '1').replace('c', '2'))
i = 0
while s[i] != '':
    j = int(s[i][0])
    s[i] = s[i][1:]
    i = j
ans = 'ABC'

print(ans[i])
