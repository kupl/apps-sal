def atc_052a(input_value: str) -> int:
    (A, B, C, D) = list(map(int, input_value.split(' ')))
    return max(A * B, C * D)


input_value = input()
print(atc_052a(input_value))
