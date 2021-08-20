import itertools


def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x


def haha(t):
    l = []
    for i in range(len(t)):
        l.append(int(t[i]))
    p = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            p += min(l[i:j + 1])
    return [p, l]


(n, m) = list(map(int, input().split()))
s = ''
for i in range(1, n + 1):
    s += str(i)
l = [1, 4, 10, 20, 35, 56, 84, 120]
x = l[n - 1]
c = 0
asdf = list(itertools.permutations(s))
for i in range(factorial(n)):
    y = haha(asdf[i])
    if y[0] == x:
        c += 1
        if c == m:
            y = y[1]
            for j in range(len(y)):
                y[j] = str(y[j])
            print(' '.join(y))
            break
