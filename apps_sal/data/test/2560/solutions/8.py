def possible(numbers):
    if int(numbers[0]) == int(numbers[1]) or int(numbers[0]) == int(numbers[2]) or (int(numbers[0]) > int(numbers[1]) and int(numbers[0]) < int(numbers[2])):
        return 'Yes'
    elif int(numbers[0]) < int(numbers[1]) or int(numbers[0]) // int(numbers[1]) < int(numbers[1]) - int(numbers[2]):
        return 'No'
    else:
        if int(numbers[0]) % int(numbers[1]) == 0 or int(numbers[0]) % int(numbers[1]) + int(numbers[1]) < int(numbers[2]) or (int(numbers[0]) % int(numbers[1]) + int(numbers[1]) * (int(numbers[0]) // int(numbers[1]) - 1) <= int(numbers[2]) and int(numbers[0]) % int(numbers[1]) + int(numbers[1]) * (int(numbers[0]) // int(numbers[1]) - 1) >= int(numbers[1])) or int(numbers[0]) % int(numbers[1]) // (int(numbers[0]) // int(numbers[1])) < int(numbers[2]) - int(numbers[1]):
            return 'Yes'
        return 'No'


for i in range(0, int(input())):
    numbers = input().split(' ')
    if i == -1 and int(numbers[0]) != 2:
        print(numbers)
    print(possible(numbers))
