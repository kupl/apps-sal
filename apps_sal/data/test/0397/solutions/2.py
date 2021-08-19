(turns, candies) = map(int, input().split())
summ = 0
turn = 0
while candies != summ - (turns - turn):
    turn += 1
    summ += turn
print(turns - turn)
