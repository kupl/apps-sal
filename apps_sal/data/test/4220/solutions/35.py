K = int(input())
S = input()
characters = len(S)
if characters <= K:
    print(S)
elif characters > K:
    print(S[:K] + '...')
