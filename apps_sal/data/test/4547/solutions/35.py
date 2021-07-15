N = str(input())

def answer(N: str) -> str:
    if '9' in N:
        return 'Yes'
    else:
        return 'No'

print(answer(N))
