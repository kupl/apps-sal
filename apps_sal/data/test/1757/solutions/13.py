f = [1, 1]
for i in range(2, 90):
    f.append(f[i - 1] + f[i - 2])
n = int(input())
for i in range(1, n + 1):
    if i in f:
        print('O', end='')
    else:
        print('o', end='')
