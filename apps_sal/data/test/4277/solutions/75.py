(ninzu, train, taxi) = map(int, input().split())
train_fare = ninzu * train
minimum_fee = min(taxi, train_fare)
print(minimum_fee)
