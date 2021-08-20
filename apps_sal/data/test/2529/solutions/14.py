(amount, balance) = list(map(float, input().split()))
if amount + 0.5 <= balance:
    if amount % 5 == 0:
        print(balance - amount - 0.5)
    else:
        print(balance)
else:
    print(balance)
