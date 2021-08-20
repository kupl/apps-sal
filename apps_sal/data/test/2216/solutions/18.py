(x, y, k) = map(int, input().split(' '))


def nxt(lst):
    a = lst[0]
    b = lst[1]
    if not (1 <= a <= x and 1 <= b <= y):
        return [-420420, -420]
    if a % 2 == 1 and b == y:
        return [a + 1, b]
    if a % 2 == 0 and b == 1:
        return [a + 1, b]
    if a % 2 == 0:
        return [a, b - 1]
    else:
        return [a, b + 1]


a = [1, 1]
for i in range(k - 1):
    a1 = a[0]
    a2 = a[1]
    a = nxt(a)
    a3 = a[0]
    a4 = a[1]
    a = nxt(a)
    print(2, a1, a2, a3, a4)
xx = []
print(x * y - 2 * (k - 1), end=' ')
while nxt(a) != [-420420, -420]:
    print(a[0], a[1], end=' ')
    a = nxt(a)
