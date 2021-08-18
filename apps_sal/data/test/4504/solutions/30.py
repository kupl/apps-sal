
S = list(input())[:-2]


def check(S):
    half = len(S) // 2
    if S[:half] == S[half:]:
        return True
    else:
        return False


while True:
    if check(S):
        print((len(S)))
        break
    S = S[:-2]
