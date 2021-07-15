numbers = input()

if numbers[1] == numbers[2]:
    if numbers.count(numbers[1]) >= 3:
        print("Yes")
        return

print("No")

