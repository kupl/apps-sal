
def atc_117b(N: int, Li_input: str) -> str:
    Li = [int(i) for i in Li_input.split(" ")]
    Li = sorted(Li)
    max_length = Li.pop()
    if max_length < sum(Li):
        return "Yes"
    return "No"


N_input_value = int(input())
Li_input_value = input()
print((atc_117b(N_input_value, Li_input_value)))
