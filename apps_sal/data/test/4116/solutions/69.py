def atc_144b(input_value: int) -> str:
    for i in range(1, 9 + 1):
        if input_value % i == 0 and input_value / i <= 9:
            return "Yes"
    return "No"


input_value = int(input())
print(atc_144b(input_value))
