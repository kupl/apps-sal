# 079a

def atc_079a(input_value: str) -> str:
    n = 3
    for i in range(0, len(input_value) + 1 - n):
        for j in range(1, n):
            if input_value[i] != input_value[i + j]:
                break
            if j == n - 1:
                return "Yes"
    return "No"

input_value = input()
print((atc_079a(input_value)))

