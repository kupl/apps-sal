N = input()
sen_yen_sheet = -(-int(N) // 1000)
money = 1000 * sen_yen_sheet

change = money - int(N)

print(change)
