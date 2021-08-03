def calc(cnt):
    return sum(sorted(num + cnt * ind for ind, num in enumerate(price, 1))[:cnt])


n, money = list(map(int, input().split()))
price = [int(num) for num in input().split()]

can = 0
cant = n + 1
while cant - can > 1:
    mid = (can + cant) // 2
    if calc(mid) <= money:
        can = mid
    else:
        cant = mid

print(can, calc(can))
