dish = [int(input()) for i in range(5)]
dish_s = [(dish[i] + 9) // 10 for i in range(5)]
dish_d = [dish[i] % 10 for i in range(5)]
sum = 0
for i in range(5):
    sum += dish_s[i]
m = 0
for i in range(5):
    if dish_s[i] * 10 - dish[i] > m:
        m = dish_s[i] * 10 - dish[i]
print(sum * 10 - m)
