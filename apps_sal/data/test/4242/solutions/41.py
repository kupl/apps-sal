a, b, k = map(int, input().split())
def answer(a: int, b: int, k: int) -> int:
    result = []
    if a > b:
        for i in range(1, b + 1):
            if a % i == 0 and b % i == 0:
                result.append(i)
        return result[len(result) - k]
    else:
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                result.append(i)
        return result[len(result) - k]

print(answer(a, b, k))
