l = input().split()
a = list(map(int, l[0]))
k = int(l[1])
n = len(a)


def rshift(a, l, r):
    t = a[r]
    for i in range(r, l, -1):
        a[i] = a[i - 1]
    a[l] = t


for i in range(n - 1):
    if k == 0:
        break
    j = min(n - 1, i + k)
    m = max(a[i + 1:j + 1])
    if m > a[i]:
        x = i + a[i + 1:j + 1].index(m) + 1
        rshift(a, i, x)
        k -= x - i
print(''.join(map(str, a)))
