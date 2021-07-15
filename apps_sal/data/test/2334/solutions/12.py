num_addresses = int(input())
addresses = list(map(int, input().split()))
max_satoshies, fee = list(map(int, input().split()))
movements = 0
for address in addresses:
    to_move = address - max_satoshies
    if to_move > 0:
        movements += to_move // (max_satoshies + fee)
        if to_move % (max_satoshies + fee) != 0:
            movements += 1
print(movements * fee)

