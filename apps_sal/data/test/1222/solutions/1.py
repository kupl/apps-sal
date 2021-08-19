k = int(input())
L = []


def f(d, now, L):
    L.append(now)
    if d == 10:
        return
    for j in range(-1, 2):
        v = now % 10 + j
        if 0 <= v <= 9:
            f(d + 1, now * 10 + v, L)


for l in range(1, 10):
    f(1, l, L)
L.sort()
print(L[k - 1])
