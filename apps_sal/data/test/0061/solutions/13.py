(n, bx) = list(map(int, input().split()))
x = list(map(int, input().split()))
(m, by) = list(map(int, input().split()))
y = list(map(int, input().split()))
x = x[::-1]
y = y[::-1]
st = 1
ansx = 0
for i in range(n):
    ansx += x[i] * st
    st *= bx
st = 1
ansy = 0
for i in range(m):
    ansy += y[i] * st
    st *= by
print('=' if ansx == ansy else '<' if ansx < ansy else '>')
