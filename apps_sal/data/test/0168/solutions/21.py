n = int(input())
a = input()
balance, min1 = 0, 0
for q in a:
    if q == '+':
        balance += 1
    else:
        balance -= 1
    min1 = min(min1, balance)
print(balance-min1)

