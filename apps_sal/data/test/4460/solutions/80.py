x = list(map(int, input().split()))
count = 0
for i in range(0, 5):
    if x[i] == 0:
        count += 1
        number = i + 1
    else:
        count += 0
print(number)
