def atc_131a(input_value: str) -> str:
    for i in range(0, len(input_value) - 1):
        if input_value[i] == input_value[i + 1]:
            return "Bad"
    return "Good"


input_value = input()
print(atc_131a(input_value))
