from collections import defaultdict

l, r, x, y = list(map(int, input().split()))

if x == y == 1:
    if l == 1:
        print(1)
        return

    print(0)
    return

if y % x != 0:
    print(0)
    return

c = x * y

c_ = y // x
i = 2
del_ = defaultdict(int)
while c_ > 1:
    while c_ % i == 0:
        c_ //= i
        del_[i] += 1

    i += 1

mas = tuple(k ** v for k, v in list(del_.items()))
ln = len(mas)

ans = 0
for i in range(2 ** ln):
    b = bin(i)[2:].zfill(ln)

    a = x
    for j in range(ln):
        if b[j] == '1':
            a *= mas[j]

    b = c // a

    if l <= a <= r and l <= b <= r:
        ans += 1

print(ans)

