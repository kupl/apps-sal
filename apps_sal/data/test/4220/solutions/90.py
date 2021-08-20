K = int(input())
S = input()
if len(S) > K:
    s = S[:K] + '...'
    print(s)
else:
    print(S)
