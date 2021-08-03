n = int(input())
s = input()
a = []
k0, k1, k2 = 0, 0, 0
for i in s:
    if i == '0':
        k0 += 1
    elif i == '1':
        k1 += 1
    else:
        k2 += 1
    a.append(i)
n1 = n // 3
if k1 == k2 and k2 == k0:
    print(s)
else:
    for i in range(n):
        if s[i] == '2':
            if k2 > n1:
                if k0 < n1:
                    a[i] = '0'
                    k0 += 1
                    k2 -= 1
                elif k1 < n1:
                    a[i] = '1'
                    k1 += 1
                    k2 -= 1
        if s[i] == '1':
            if k1 > n1:
                if k0 < n1:
                    a[i] = '0'
                    k0 += 1
                    k1 -= 1
    for i in range(n - 1, -1, -1):
        if a[i] == '0':
            if k0 > n1:
                if k2 < n1:
                    a[i] = '2'
                    k2 += 1
                    k0 -= 1
                elif k1 < n1:
                    a[i] = '1'
                    k1 += 1
                    k0 -= 1
        if a[i] == '1':
            if k1 > n1:
                if k2 < n1:
                    a[i] = '2'
                    k2 += 1
                    k1 -= 1
    for i in a:
        print(i, end='')
