# coding=utf-8

q = int(input())

a = [0 for i in range(2 * 10 ** 5 + 1)]
base = 0
l = -1
r = 1
input()
k = 0

for i in range(q - 1):
    s = input().split()
    b = int(s[1])

    if s[0] == 'L':
        a[b] = l
        l -= 1
        base += 1
        k += 1
    elif s[0] == 'R':
        a[b] = r
        r += 1
        k += 1
    else:
        ind = a[b] + base
        print(min(ind, k - ind))
