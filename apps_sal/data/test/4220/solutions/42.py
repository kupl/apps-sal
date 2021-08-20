K = int(input())
S = str(input())
if len(S) <= K:
    print(S)
else:
    ans = S[:K] + '...'
    print(ans)
