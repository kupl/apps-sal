#!/user/bin/env/python 3.5
# ---*--- code:utf-8 ---*---

n, k, x = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
b = []
i = 0
while i < k:
    a.sort()
    c = list()
    for each in a:
        c.append(each)
    b.append(c)
    if i - 4 >= 0 and b[i] == b[i - 4]:
        break
    for j in range(0, n, 2):
        a[j] = a[j] ^ x
    i = i + 1
a.sort()
if i == k:
    print(a[-1], a[0])
else:
    print(b[(k - i + 4) % 4 + i - 4][-1], b[(k - i + 4) % 4 + i - 4][0])
