K = int(input())
S = input()
if len(S) <= K:
    print(S)
    return
else:
    print(S[:K] + '...')
    return
