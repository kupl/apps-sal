from collections import deque

k = int(input())

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = deque(a)

while b:
    v = b.popleft()
    if v % 10 == 0:
        f = v * 10 + 1
        if f <= 3234566667:

            b.append(f)
            a.append(f)
        g = v * 10
        if g <= 3234566667:
            b.append(g)
            a.append(g)

    elif v % 10 == 9:
        f = v * 10 + 8
        g = v * 10 + 9
        if f <= 3234566667:

            b.append(f)
            a.append(f)
        if g <= 3234566667:
            b.append(g)
            a.append(g)

    else:
        f = v * 10 + (v % 10) - 1
        g = v * 10 + (v % 10)
        h = v * 10 + (v % 10) + 1
        if f <= 3234566667:
            b.append(f)
            a.append(f)
        if g <= 3234566667:
            b.append(g)
            a.append(g)
        if h <= 3234566667:
            b.append(h)
            a.append(h)

a.sort()

print(a[k - 1])
