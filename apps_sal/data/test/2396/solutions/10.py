n = int(input())
dicti = {}
L = []
for i in range(n):
    s = input()
    a = ''
    b = ''
    c = ''
    i = 1
    while s[i] != '+':
        a += s[i]
        i = i + 1
    i = i + 1
    while s[i] != ')':
        b += s[i]
        i = i + 1
    c = s[i + 2:]

    a, b, c = int(a), int(b), int(c)
    res = (a + b) / c
    if res in dicti:
        dicti[res] += 1
    else:
        dicti[res] = 1
    L.append(res)

for i in range(len(L)):
    print(dicti[L[i]], end=' ')
