def atc_059a(input_value: str) -> str:
    S = input_value.split(" ")
    SSS = S[0][0].upper() + S[1][0].upper() + S[2][0].upper()
    return SSS

input_value = input()
print((atc_059a(input_value)))

