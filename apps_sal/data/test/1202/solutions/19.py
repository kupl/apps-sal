n = int(input())
a = []
b = []
for i in range(n):
    pair = input().split()
    a.append(int(pair[0]))
    b.append(int(pair[1]))
flag = 0
for i in range(n):
    if i < n // 2:
        print('1', end='')
    else:
        if flag == 0 and a[i] >= b[n - i - 1]:
            flag = 1
        if flag == 0:
            print('1', end='')
        else:
            print('0', end='')
print()
flag = 0
for i in range(n):
    if i < n // 2:
        print('1', end='')
    else:
        if flag == 0 and b[i] >= a[n - i - 1]:
            flag = 1
        if flag == 0:
            print('1', end='')
        else:
            print('0', end='')
