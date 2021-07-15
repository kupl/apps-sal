N = int(input())
from collections import Counter
S = [Counter(list(input())) for _ in range(N)]

def intersection(X):
    Res = X[0]
    if len(X) == 1:
        return Res
    for x in X[1:]:
        Res = {k:min(Res[k],x[k]) for k in Res if k in x}
    return Counter(Res)

print((''.join(sorted(intersection(S).elements()))))

