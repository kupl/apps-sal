
def atc_089b(input_value: str) -> str:
    N = input_value[0]
    Si = input_value[1]
    colors = ["P" in Si, "W" in Si, "G" in Si, "Y" in Si]
    if colors.count(True) == 3:
        return "Three"
    elif colors.count(True) == 4:
        return "Four"
    else:
        return "other"


N_input = input()
Si_input = input()
print(atc_089b([N_input, Si_input]))
