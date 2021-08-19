(n, bx) = list(map(int, input().split()))
b = list(map(int, input().split()))
ansx = 0
for i in range(n - 1, -1, -1):
    ansx += b[i] * bx ** (n - i - 1)
(m, by) = list(map(int, input().split()))
b = list(map(int, input().split()))
ansy = 0
for i in range(m - 1, -1, -1):
    ansy += b[i] * by ** (m - i - 1)
if ansx == ansy:
    print('=')
elif ansx > ansy:
    print('>')
else:
    print('<')
