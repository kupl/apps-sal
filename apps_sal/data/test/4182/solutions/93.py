n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.append(x)
b.append(y)
a = sorted(a)
b = sorted(b)
if a[-1] < b[0]:
    print('No War')
else:
    print('War')
