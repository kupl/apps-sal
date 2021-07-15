a, b, c = map(int, input().split())

def answer(a: int, b: int, c: int) -> int:
    return min(a + b, a + c, b + c)

print(answer(a, b, c))
