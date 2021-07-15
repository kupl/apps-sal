total_price = int(input())
num_one_coin = int(input())

mod = total_price % 500

if num_one_coin >= mod:
    print('Yes')
else:
    print('No')
