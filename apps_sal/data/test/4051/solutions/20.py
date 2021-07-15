def topple(a):
    for i in range(1, len(a)):
        if a[i] - 2 >= a[i - 1]:
            a[i] -= 1
            a[i - 1] += 1
        elif a[i] + 2 <= a[i - 1]:
            a[i - 1] -= 1
            a[i] += 1

    return a

def ravioli(a):
    res = []
    while a:
        a = topple(a)
        best = 0 
        for i in range(len(a)):
            if a[i] > a[best]:
                best = i
        res.append(a[best])
        a = a[:best] + a[best + 1:]

    return list(reversed(res))

n = int(input())
a = list(map(int, input().split()))
b = list(a)
b.sort()

c = ravioli(a)
if b == c:
    print('YES')
else:
    print('NO')

