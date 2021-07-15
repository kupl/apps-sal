def atc_142b(NK_input: str, hi_input: str) -> int:
    N, K = map(int, NK_input.split(" "))
    hi = [int(i) for i in hi_input.split(" ")]
    hi = sorted(hi)
    for i in range(0, len(hi)):
        if hi[i] >= K:
            return len(hi) - i
    return 0


NK_input_value = input()
hi_input_value = input()
print(atc_142b(NK_input_value, hi_input_value))
