string = input()
sum = 0
for a in string:
    if a == '+':
        sum += 1
    elif a == '-':
        sum -= 1
print(sum)
