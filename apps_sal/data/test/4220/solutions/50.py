K = int(input())
S = str(input())
N = len(S)
if N <= K:
    print(S)
else:
    print(S[:K] + '...')
