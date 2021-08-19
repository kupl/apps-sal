req = int(input())
for i in range(req):
    (amount, edit) = map(int, input().split())
    price = list(map(int, input().split()))
    price.sort()
    if amount == 1:
        print(price[0] + edit)
    elif price[0] + edit >= price[-1] - edit:
        print(price[0] + edit)
    else:
        print(-1)
