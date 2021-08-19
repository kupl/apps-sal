def atc_042a(input_value: str) -> str:
    ABC = input_value.split(' ')
    if ABC.count('5') == 2 and ABC.count('7') == 1:
        return 'YES'
    return 'NO'


input_value_1 = input()
print(atc_042a(input_value_1))
