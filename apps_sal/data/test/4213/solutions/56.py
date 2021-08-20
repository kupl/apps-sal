def atc_102b(N: int, Ai_input: str) -> int:
    Ai = [int(i) for i in Ai_input.split(' ')]
    return max(Ai) - min(Ai)


N_input_value = int(input())
Ai_input_value = input()
print(atc_102b(N_input_value, Ai_input_value))
