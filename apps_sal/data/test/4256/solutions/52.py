
# 120a

def atc_120a(input_value: str) -> int:
    A, B, C = map(int, input_value.split(" "))
    return min(C, B // A)


input_value = input()
print(atc_120a(input_value))
