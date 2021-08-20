n = int(input())
l = list(input())
a = [0] * 10
for i in l:
    if i == 'L':
        j = 0
        while a[j] != 0:
            j += 1
        a[j] = 1
    elif i == 'R':
        j = 9
        while a[j] != 0:
            j -= 1
        a[j] = 1
    else:
        a[int(i)] = 0
print(''.join([str(i) for i in a]))
