(x, k) = input().split()
x = int(x)
k = int(k)
a = list(map(int, input().split()))
b = []
aumento = 0
for i in range(k):
    y = list(map(int, input().split()))
    if y[0] == 1:
        a[y[1] - 1] = y[2] - aumento
    elif y[0] == 2:
        aumento += y[1]
    else:
        b.append(str(a[y[1] - 1] + aumento))
print('\n'.join(b))
