(x, y, z) = list(map(int, input().split()))
can_buy = x // z
can_buy += y // z
x %= z
y %= z
ans = 0
if x + y >= z:
    can_buy += 1
    ans = z - max(x, y)
print('{} {}'.format(can_buy, ans))
