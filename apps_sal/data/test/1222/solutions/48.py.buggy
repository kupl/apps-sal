# ABC161

k = int(input())

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


while(True):
    if k <= len(a):
        print((a[k - 1]))
        return
    k -= len(a)
    b = list()
    a, b = b, a
    for x in b:
        for i in range(-1, 2):
            d = x % 10 + i
            if d < 0 or d > 9:
                continue
            nx = x * 10 + d
            a.append(nx)
