def atc_120b(ABK: str) -> int:
    (a, b, k) = map(int, ABK.split(' '))
    result_value = min(a, b)
    letter_count = 0
    for i in range(result_value, 0, -1):
        if a % i == 0 and b % i == 0:
            letter_count += 1
        if letter_count == k:
            break
    return i


ABK_input = input()
print(atc_120b(ABK_input))
