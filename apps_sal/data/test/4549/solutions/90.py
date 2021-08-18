h, w = map(int, input().split())
a = ['.' * (w + 2)]
s = ['.' + input() + '.' for _ in range(h)]
s = a + s + a
f = True
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '
        f = False
if f:
    print('Yes')
else:
    print('No')
