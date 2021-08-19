def answer(k: int, s: str) -> str:
    if len(s) <= k:
        return s
    else:
        return s[:k] + '...'


k = int(input())
s = input()
print(answer(k, s))
