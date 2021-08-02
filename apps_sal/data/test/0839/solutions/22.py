def next(a):
    k = len(a) - 2

    while a[k] > a[k + 1]:
        k -= 1;

    t = k + 1

    while t < len(a) - 1 and a[t + 1] > a[k]:
        t += 1

    a[t], a[k] = a[k], a[t]

    sub = a[k + 1:]
    sub.reverse()

    res = a[:k + 1] + sub

    return res


def countCurrent(a, happiness):
    res = 0

    for i in range(len(a) // 2):
        f = a[2 * i]
        n = a[2 * i + 1]
        res += happiness[f][n] + happiness[n][f]

    return res


def count(a, happiness):
    res = 0
    tmp = a

    while len(tmp) > 1:
        res += countCurrent(tmp, happiness)
        tmp = tmp[1:]

    return res


happiness = []

for x in range(5):
    happiness.append([int(c) for c in input().split()])

test = [0, 1, 2, 3, 4]
k = 0

while True:
    c = count(test, happiness)
    if c > k:
        k = c
    if test != [4, 3, 2, 1, 0]:
        test = next(test)
    else:
        break

print(k)
