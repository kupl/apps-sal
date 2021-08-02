from sys import stdin, stdout


sze = 10 ** 5
power = []
for i in range(sze):
    power.append(i * i)


def sqrt(v):
    l, r = 0, sze

    while (r - l > 1):
        m = (l + r) >> 1

        if power[m] <= v:
            l = m
        else:
            r = m

    return l


def add_f(v):
    if not v:
        first.append(2)
    else:
        first.append(1)


def add_s(v):
    l, r = 0, sze

    while r - l > 1:
        m = (l + r) >> 1

        if power[m] <= v:
            l = m
        else:
            r = m

    second.append(min(v - power[l], power[r] - v))


n = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
first, second = [], []

for v in values:
    a = sqrt(v)

    if a * a == v:
        add_f(v)
    else:
        add_s(v)

first.sort()
second.sort()
ans = 0

k = n // 2

if len(first) < len(second):
    for i in range(k - len(first)):
        ans += second[i]
elif len(first) > len(second):
    for i in range(k - len(second)):
        ans += first[i]

stdout.write(str(ans))
