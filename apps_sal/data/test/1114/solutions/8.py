(n, m) = map(int, input().split())
f = []
b = []
x = []
y = []
f = list(map(int, input().split()))
for i in range(n):
    x.append(0)
    y.append(0)
for i in range(n):
    x[f[i] - 1] = x[f[i] - 1] + 1
    y[f[i] - 1] = i + 1
b = list(map(int, input().split()))
amb = 0
imp = 0
for i in range(m):
    if x[b[i] - 1] > 1:
        amb = 1
    elif x[b[i] - 1] == 0:
        imp = 1
if imp > 0:
    print('Impossible')
elif amb > 0:
    print('Ambiguity')
elif 1 == 1:
    print('Possible')
    for i in range(m):
        print(str(y[b[i] - 1]) + ' ', end='')
