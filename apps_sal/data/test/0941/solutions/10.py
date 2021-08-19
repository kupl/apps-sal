(b, k) = map(int, input().split())
l = [*map(int, input().split())]
l.reverse()
res = 0
for (i, e) in enumerate(l):
    res = (res + e * pow(b, i, 2)) % 2
if res == 0:
    print('even')
else:
    print('odd')
