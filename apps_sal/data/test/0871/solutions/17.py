(n, s) = map(int, input().split(' '))
l = list()
for i in range(n):
    (a, b) = map(int, input().split(' '))
    l.append(a * 60 + b)
if l[0] - s >= 1:
    print(0, 0)
else:
    for i in range(n - 1):
        t = l[i + 1] - l[i] - 1 - 2 * s
        if t >= 1:
            tt = l[i] + 1 + s
            (h, m) = (tt // 60, tt % 60)
            print(h, m)
            break
    else:
        tt = l[-1] + 1 + s
        (h, m) = (tt // 60, tt % 60)
        print(h, m)
