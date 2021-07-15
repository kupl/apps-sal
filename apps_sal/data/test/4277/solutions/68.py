  
# 133a

def atc_133a(input_value: str) -> int:
    NAB = input_value.split(" ")
    N = int(NAB[0])
    A = int(NAB[1])
    B = int(NAB[2])

    return min(N * A, B)


input_value = input()
print(atc_133a(input_value))
