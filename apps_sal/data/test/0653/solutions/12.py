n = int(input())
s = input()

a = [0] * 10
for i in s:
    if i == 'L':
        for j in range(10):
            if a[j] == 0:
                a[j] = 1
                break
    elif i == 'R':
        for j in range(9, -1, -1):
            if a[j] == 0:
                a[j] = 1
                break
    else:
        a[int(i)] = 0

for i in a:
    print(i, end = '')

