details = []
for i in range(5):
    details.append(int(input()))
new_list = []
for i in range(10):
    current = 10 - i
    for numbers in details:
        if (((numbers - current) % 10) == 0):
            new_list.append(numbers)
counter = 0
for numbers in new_list[:len(new_list)-1]:
    current = numbers
    while ((current % 10 != 0)):
        current += 1
    counter += current

print(counter + new_list[-1])
