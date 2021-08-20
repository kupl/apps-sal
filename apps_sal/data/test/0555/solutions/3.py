n = input()
digits = []
for letter in n:
    digits.append(int(letter))
for i in range(len(digits)):
    if i == 0:
        if digits[i] == 9:
            pass
        elif digits[i] > 4:
            digits[i] = 9 - digits[i]
    elif digits[i] > 4:
        digits[i] = 9 - digits[i]
for element in digits:
    print(element, end='')
