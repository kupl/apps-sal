inputs = input().split()
amount = int(inputs[0])
account = float(inputs[1])
if amount % 5 == 0 and account >= amount + 0.5:
    balance = account - amount - 0.5
    print('%.2f' % balance)
else:
    print('%.2f' % account)
