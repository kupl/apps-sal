n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = []
a.sort()
li = 0
i = 1
k = 0
la = len(a)

while i <= m:
    if li < la and a[li] < i:
        li += 1
    elif li < la and a[li] == i:
        i += 1
    else:
        m -= i
        k += 1
        b.append(i)
        i += 1

print(k)
for it in b:
    print(it, end=' ')

