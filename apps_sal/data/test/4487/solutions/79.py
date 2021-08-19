def atc_060a(input_value: str) -> str:
    (A, B, C) = map(str, input_value.split(' '))
    if A[-1] == B[0] and B[-1] == C[0]:
        return 'YES'
    else:
        return 'NO'


input_value = input()
print(atc_060a(input_value))
