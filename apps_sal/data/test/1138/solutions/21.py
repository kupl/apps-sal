s = list(input())
d = s.count('D')
l = s.count('L')
r = s.count('R')
u = s.count('U')
if len(s) % 2 != 0:
    print('-1')
else:
    print(int(abs(l - r) / 2 + abs(u - d) / 2))
