train_len, target_vehicle = list(map(int, input().split()))

target_from_backside = train_len - (target_vehicle - 1)
print(target_from_backside)

