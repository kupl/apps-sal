x = input()
y = input()

a = 'qwertyuiop' + 'asdfghjkl;' + 'zxcvbnm,./'


if x == 'R':
    for i in range(len(y)):
        t = a.index(y[i])
        print(a[t - 1], end="")
if x == 'L':
    for i in range(len(y)):
        t = a.index(y[i])
        print(a[t + 1], end="")
