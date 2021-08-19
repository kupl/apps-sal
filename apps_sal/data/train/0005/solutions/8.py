def per(X):
    S = set(X)
    if not len(X) == len(S):
        return False
    for i in range(1, len(X) + 1):
        if i not in S:
            return False
    return True


for y in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    m = max(L)
    r = []
    if n != m:
        if per(L[:m]) and per(L[m:]):
            r.append((m, n - m))
        if per(L[-m:]) and per(L[:-m]):
            r.append((n - m, m))
    r = list(set(r))
    print(len(r))
    for (a, b) in r:
        print(a, b)
