n = int(input())
p = [int(input()) for _ in range(n)]

def answer(n: int, p: int) -> int:
    a = sum(p) - max(p) // 2
    return a

print(answer(n, p))
