# 116a

def atc_116a(input_value: str) -> int:
    tri_length = [int(ai) for ai in input_value.split(" ")]
    tri_length.sort()
    return int((tri_length[0] * tri_length[1] / 2))

input_value = input()
print(atc_116a(input_value))
