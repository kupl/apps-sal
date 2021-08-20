a = input('').split(' ')
n = int(a[0])
c = int(a[1])
t = []
for i in range(n):
    t.append([0, 10 ** 5])
a = list(map(int, input('').split(' ')))
b = list(map(int, input('').split(' ')))
print(0, end=' ')
for i in range(1, n, 1):
    t[i][0] = min(t[i - 1][1], t[i - 1][0]) + a[i - 1]
    t[i][1] = min(t[i - 1][0] + c, t[i - 1][1]) + b[i - 1]
    print(min(t[i][0], t[i][1]), end=' ')
