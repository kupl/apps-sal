X = int(input())
A = int(input())
B = int(input())

balance = X - A

quantity = balance // B

balance -= B * quantity

print(balance)
