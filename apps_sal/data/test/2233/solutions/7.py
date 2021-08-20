K = int(input())
for _ in range(K):
    N = int(input())
    S = input()
    T = input()
    diff = []
    for (c1, c2) in zip(S, T):
        if c1 != c2:
            diff.append((c1, c2))
    f = False
    if len(diff) == 2:
        ((a, b), (c, d)) = diff
        if a == c and b == d:
            f = True
    print('Yes' if f else 'No')
