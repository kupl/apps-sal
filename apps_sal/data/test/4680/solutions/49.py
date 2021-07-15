a = map(int, input().split())

def answer(a: list) -> str:
    a = sorted(a)
    if a == [5, 5, 7]:
        return 'YES'
    else:
        return 'NO'

print(answer(a))
