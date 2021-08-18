

def atc_155b(input_value: str) -> str:
    N = int(input_value[0])
    Ai = [int(ai) for ai in input_value[1].split(" ")]
    for i in range(0, N):
        if Ai[i] % 2 == 0 and Ai[i] % 3 != 0 and Ai[i] % 5 != 0:
            return "DENIED"
    return "APPROVED"


N = input()
Ai = input()
print((atc_155b([N, Ai])))
