n = int(input())
a = [int(x) for x in input().split()]

price = 0
if 0 in a:
    for i in range(n):
        if a[i] != 0: price += abs(a[i]) - 1
        else: price += 1
    print(price)
else:
    cnt = 0
    for i in range(n):
        price += abs(a[i]) - 1
        cnt += a[i] < 0
    print(price + 2 * (cnt % 2))


