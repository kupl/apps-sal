z1 = list(map(int, input().split()))
x = list(map(int, input().split()))
z2 = list(map(int, input().split()))
y = list(map(int, input().split()))
(n1, b1) = (z1[0], z1[1])
(n2, b2) = (z2[0], z2[1])
ansx = ansy = 0
for i in range(n1):
    ansx += x[n1 - i - 1] * b1 ** i
for i in range(n2):
    ansy += y[n2 - i - 1] * b2 ** i
if ansx == ansy:
    print('=')
elif ansx > ansy:
    print('>')
else:
    print('<')
