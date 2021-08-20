n = int(input())
a = input()
count = 0
flag = 0
b = [int(r) for r in input().split()]
i = int()
for i in range(0, n, 1):
    if i == 0:
        if a[i] == '>':
            count = count + b[i]
        else:
            count = count - b[i]
    elif a[count] == '>':
        count += b[count]
    else:
        count -= b[count]
    if count >= n or count < 0:
        flag = 1
        break
if flag == 1:
    print('FINITE')
else:
    print('INFINITE')
