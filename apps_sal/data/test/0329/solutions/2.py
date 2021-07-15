s = input()
ne = s.count('e')//3
nn = (s.count('n')-1) // 2
ni = s.count('i')
nt = s.count('t')
m = min(ne,nn,ni,nt)
if m < 0: m = 0
print(m)
