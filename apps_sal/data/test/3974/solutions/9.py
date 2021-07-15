s = input()
low = 0
high = 0
sum = 0
for i in s:
    if i == '+':
        sum += 1
    else:
        sum -= 1
    if sum < low:
        low = sum
    if sum > high:
        high = sum
print(high - low)
