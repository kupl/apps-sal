def atc_136a(input_v: str) -> int:
    ABC = input_v.split(' ')
    A = int(ABC[0])
    B = int(ABC[1])
    C = int(ABC[2])
    D = C - (A - B)
    if D < 0:
        return 0
    else:
        return D


abc = input()
print(atc_136a(abc))
