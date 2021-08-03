A, B, X = map(int, input().split())


def isPurchasable(x):
    cost = A * x + B * len(str(x))
    return cost <= X


if not isPurchasable(1):
    print(0)
    return

if isPurchasable(10**9):
    print(10**9)
    return

ok = 1
ng = 10**9

while(abs(ng - ok) > 1):
    number = (ok + ng) // 2
    if isPurchasable(number):
        ok = number
    else:
        ng = number

ans = ok
print(ans)
