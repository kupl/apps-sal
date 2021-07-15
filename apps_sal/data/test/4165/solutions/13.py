n = int(input())
l = list(map(int, input().split()))

def answer(n: int, l: list) -> str:
    if max(l) < (sum(l) - max(l)):
        return 'Yes'
    else:
        return 'No'

print(answer(n, l))
