# 066a

def atc_066a(abc: str) -> int:
    abc_int = [int(ai) for ai in abc.split(" ")]
    abc_int.sort()
    return abc_int[0] + abc_int[1]

abc = input()
print(atc_066a(abc))
