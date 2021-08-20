n = int(input())
a = list(input())
x = a.count('0')
y = a.count('1')
z = a.count('2')
if x < n // 3:
    for i in range(n):
        if a[i] == '1' and y > n // 3:
            a[i] = '0'
            y -= 1
            x += 1
        elif a[i] == '2' and z > n // 3:
            a[i] = '0'
            z -= 1
            x += 1
        if x == n // 3:
            break
if z < n // 3:
    for i in range(n - 1, -1, -1):
        if z == n // 3:
            break
        if a[i] == '1' and y > n // 3:
            a[i] = '2'
            y -= 1
            z += 1
        elif a[i] == '0' and x > n // 3:
            a[i] = '2'
            z += 1
            x -= 1
if y < n // 3:
    for i in range(n):
        if a[i] == '2' and z > n // 3:
            a[i] = '1'
            z -= 1
            y += 1
    for i in range(n - 1, -1, -1):
        if a[i] == '0' and x > n // 3:
            a[i] = '1'
            y += 1
            x -= 1
print(''.join(a))
