# 094b

def atc_094b(NMX: str, Ai_input: str) -> int:
    N, M, X = list(map(int, NMX.split(" ")))
    Ai = [int(ai) for ai in Ai_input.split(" ")]

    up_cost = 0
    down_cost = 0

    for i in range(X + 1, N + 1):
        if i in Ai:
            up_cost += 1
    for i in range(X - 1, 0, -1):
        if i in Ai:
            down_cost += 1
    return min(up_cost, down_cost)


NMX_input_value = input()
Ai_input_value = input()
print((atc_094b(NMX_input_value, Ai_input_value)))
