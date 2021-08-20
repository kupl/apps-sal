foods = [0] * 5
sumfoods = 0
for i in range(5):
    foods[i] = int(input())
maxDiv = 0
for (i, var) in enumerate(foods):
    temp = 10 - var % 10
    if temp == 10:
        temp = 0
    foods[i] += temp
    sumfoods += foods[i]
    if maxDiv < temp:
        maxDiv = temp
print(sumfoods - maxDiv)
