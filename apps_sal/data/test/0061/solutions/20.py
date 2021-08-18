
n, bx = map(int, input().split())
x = list(map(int, input().split()))

m, by = map(int, input().split())
y = list(map(int, input().split()))

xx = sum(v * bx**(len(x) - i - 1) for i, v in enumerate(x))
yy = sum(v * by**(len(y) - i - 1) for i, v in enumerate(y))

if xx < yy:
    print('<')
elif xx == yy:
    print('=')
else:
    print('>')
