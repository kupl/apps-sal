# 092a

def atc_092a(ABCD: int) -> int:
    return min(ABCD[0], ABCD[1]) + min(ABCD[2], ABCD[3])


A = int(input())
B = int(input())
C = int(input())
D = int(input())

ABCD = [A, B, C, D]
print(atc_092a(ABCD))
