# 064b

def atc_064b(input_value: str) -> str:
    N = input_value[0]
    ai = [int(i) for i in input_value[1].split(" ")]
    return max(ai) - min(ai)

N = input()
ai = input()
print(atc_064b([N, ai]))
