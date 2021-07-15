req = int(input())
for i in range(req):
    battery, amount, a, b = map(int, input().split())
    battery -= 1
    maximum = battery // b
    if maximum < amount:
        print(-1)
    else:
        c = a - b
        battery -= b * amount
        print(min(battery // c, amount))
