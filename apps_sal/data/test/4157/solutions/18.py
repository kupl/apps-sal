def to(a):
    s = 0
    while a % 2 == 0 and a != 0:
        s += 1
        a = a // 2
    return s


def tr(a):
    s = 0
    while a % 3 == 0 and a != 0:
        s += 1
        a = a // 3
    return s


n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(i + 1, n):
        if to(a[i]) > to(a[j]):
            (a[i], a[j]) = (a[j], a[i])
        if tr(a[i]) < tr(a[j]):
            (a[i], a[j]) = (a[j], a[i])
print(*a)
