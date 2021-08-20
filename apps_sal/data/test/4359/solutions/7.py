cooktime = []
min_index = 100
min = 123
for i in range(5):
    cooktime.append(int(input('')))
    if cooktime[i] % 10 != 0 and min > cooktime[i] % 10:
        min_index = i
        min = cooktime[i] % 10
sum = 0
for i in range(5):
    sum += cooktime[i]
    if i != min_index and cooktime[i] % 10 != 0:
        sum += 10 - cooktime[i] % 10
print(str(sum))
