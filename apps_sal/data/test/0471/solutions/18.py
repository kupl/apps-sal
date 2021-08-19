(n, a) = list(map(int, input().split(' ')))
x = list(map(int, input().split(' ')))
(MAX, MIN) = (1000000, -1000000)
(r1, r2, l1, l2) = (MIN - 1, MIN - 1, MAX + 1, MAX + 1)
for xi in x:
    if xi <= l1:
        l2 = l1
        l1 = xi
    elif xi < l2:
        l2 = xi
    if xi >= r1:
        r2 = r1
        r1 = xi
    elif xi > r2:
        r2 = xi
if n == 1:
    print(0)
else:
    print(min(r1 - l2 + abs(a - r1), r1 - l2 + abs(a - l2), r2 - l1 + abs(a - r2), r2 - l1 + abs(a - l1)))
