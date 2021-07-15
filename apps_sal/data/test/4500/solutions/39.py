a_coin, b_coin, price = map(int, input().split())

if a_coin + b_coin >= price:
    print('Yes')
else:
    print('No')
