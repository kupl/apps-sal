

def atc_115b(N: int, Pi_input: int) -> int:
    Pi_input = sorted(Pi_input)
    max_price = Pi_input.pop()
    return int(sum(Pi_input) + max_price / 2)


N_input_value = int(input())
Pi_input_value = []
for i in range(0, N_input_value):
    Pi_input_value.append(int(input()))
print(atc_115b(N_input_value, Pi_input_value))
