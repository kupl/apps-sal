from collections import Counter
S = list(input())
S = Counter(S)
ans = S["+"]-S["-"]
print(ans)

