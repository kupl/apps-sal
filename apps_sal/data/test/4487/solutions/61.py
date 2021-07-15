A, B, C = input().split()

def answer(A: int, B: int, C: int) -> str:
    if A[-1] == B[0] and B[-1] == C[0]:
        return 'YES'
    else:
        return 'NO'

print((answer(A, B, C)))

