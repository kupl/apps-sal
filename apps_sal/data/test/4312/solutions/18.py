A, B, C, D = list(map(int, input().split()))

def answer(A: int, B: int, C: int, D: int) -> str:
    while True:
        C -= B
        if C <= 0:
            return "Yes"
            break

        A -= D
        if A <= 0:
            return "No"
            break

print((answer(A, B, C, D)))

