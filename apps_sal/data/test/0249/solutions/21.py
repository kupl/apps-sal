n, l, x, y = list(map(int, input().split(" ")))
li = list(map(int, input().split(" ", n)[:n]))
li.sort()
dic = {}
a1, a2 = 0, 0
ans = 2
x1 = x
y1 = y
xi = -1
yi = -1
for i in li:
    dic[i] = 1
for i in range(n):
    if li[i] - x >= 0:
        if li[i] - x in dic:
            a1 = 1
            xi = i
    if li[i] + x <= l:
        if li[i] + x in dic:
            a1 = 1
            xi = i
    if li[i] - y >= 0:
        if li[i] - y in dic:
            a2 = 1
            yi = i
    if li[i] + y <= l:
        if li[i] + y in dic:
            a2 = 1
            yi = i
if a1 == 1 and a2 == 1:
    print(0)
elif a1 == 1:
    if li[xi] - x >= 0:
        if li[xi] - x in dic:
            if li[xi] - x + y <= l and li[xi] - x + y in dic:
                a2 = 1
            if li[xi] - x - y >= 0 and li[xi] - x - y in dic:
                a2 = 1
    if li[xi] + x <= l:
        if li[xi] + x in dic:
            if li[xi] + x + y <= l and li[xi] + x + y in dic:
                a2 = 1
            if li[xi] + x - y >= 0 and li[xi] + x - y in dic:
                a2 = 1
    if a2 == 1:
        print(0)
    else:
        print(1)
        print(y)
elif a2 == 1:
    if li[yi] - y >= 0:
        if li[yi] - y in dic:
            if li[yi] - y + x <= l and li[yi] - y + x in dic:
                a1 = 1
            if li[yi] - y - x >= 0 and li[yi] - y - x in dic:
                a1 = 1
    if li[yi] + y <= l:
        if li[yi] + x in dic:
            if li[yi] + y + x <= l and li[yi] + y + x in dic:
                a1 = 1
            if li[yi] + y - x >= 0 and li[yi] + y - x in dic:
                a1 = 1
    if a1 == 1:
        print(0)
    else:
        print(1)
        print(x)
else:
    for i in range(n):
        if li[i] - x >= 0:
            a1 = 1
            xi = i
            if li[xi] - x + y <= l and li[xi] - x + y in dic:
                a2 = 1
            if li[xi] - x - y >= 0 and li[xi] - x - y in dic:
                a2 = 1
            if a2 == 1:
                print(1)
                print(li[i] - x)
                break
            else:
                a1 = 0
        if li[i] + x <= l:
            a1 = 1
            xi = i
            if li[xi] + x + y <= l and li[xi] + x + y in dic:
                a2 = 1
            if li[xi] + x - y >= 0 and li[xi] + x - y in dic:
                a2 = 1
            if a2 == 1:
                print(1)
                print(li[i] + x)
                break
            else:
                a1 = 0
        if li[i] - y >= 0:
            a2 = 1
            yi = i
            if li[yi] - y + x <= l and li[yi] - y + x in dic:
                a1 = 1
            if li[yi] - y - x >= 0 and li[yi] - y - x in dic:
                a1 = 1
            if a1 == 1:
                print(1)
                print(li[i] - y)
                break
            else:
                a2 = 0
        if li[i] + y <= l:
            a2 = 1
            yi = i
            if li[yi] + y + x <= l and li[yi] + y + x in dic:
                a1 = 1
            if li[yi] + y - x >= 0 and li[yi] + y - x in dic:
                a1 = 1
            if a1 == 1:
                print(1)
                print(li[i] + y)
                break
            else:
                a2 = 0
if a1 == 0 and a2 == 0:
    print(2)
    print(x, y)
