def solve(s):
    T = {}
    for c in 'Bulbasaur':
        if c in T:
            T[c] += 1
        else:
            T[c] = 1

    S = len(s)
    for c in T:
        S = min(S, s.count(c) // T[c])

    return S


s = input().rstrip()
print(solve(s))
