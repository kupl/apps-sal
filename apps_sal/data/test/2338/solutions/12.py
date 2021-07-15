import sys
input = sys.stdin.readline
I = lambda : list(map(int,input().split()))

n,=I()
seg = [I() for _ in range(n)]
seg = sorted(seg, key=lambda x : abs(x[0]) + abs(x[1]))
res = []
for x, y in seg:
    if x > 0: res.append('1 %d %c' % (x, 'R'))
    if x < 0: res.append('1 %d %c' % (-x, 'L'))
    if y > 0: res.append('1 %d %c' % (y, 'U'))
    if y < 0: res.append('1 %d %c' % (-y, 'D'))
    res.append('2')
    if x > 0: res.append('1 %d %c' % (x, 'L'))
    if x < 0: res.append('1 %d %c' % (-x, 'R'))
    if y > 0: res.append('1 %d %c' % (y, 'D'))
    if y < 0: res.append('1 %d %c' % (-y, 'U'))
    res.append('3')    
print(len(res))
print('\n'.join(res))

