n = int(input())
a = list(map(int, input().split()))


def f(a):
    mm = float('-inf')
    for x in range(len(a) - 1):
        mm = max(mm, a[x + 1] - a[x])
    return mm


(ans, ansx) = (-1, float('+inf'))
for i in range(1, n - 1):
    nn = f(a[:i] + a[i + 1:])
    if nn < ansx:
        (ans, ansx) = (i, nn)
print(ansx)
