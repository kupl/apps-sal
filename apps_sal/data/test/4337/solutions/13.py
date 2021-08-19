N = int(input())
S = str(input())


def ans089(N: int, S: list):
    S = S.split()
    if len(set(S)) == 4:
        return 'Four'
    elif len(set(S)) == 3:
        return 'Three'


print(ans089(N, S))
