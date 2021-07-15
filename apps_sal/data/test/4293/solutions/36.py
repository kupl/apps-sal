# 129a

def atc_129a(input_value: str) -> int:
    PQR = input_value.split(" ")
    P = int(PQR[0])
    Q = int(PQR[1])
    R = int(PQR[2])

    return min(P + Q, P + R, Q + R)

input_value = input()
print(atc_129a(input_value))
