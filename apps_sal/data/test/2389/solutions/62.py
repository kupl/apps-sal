def main():
    (N, A, B, C) = list(map(int, input().split()))
    S = [{'AB': (0, 1), 'BC': (1, 2), 'AC': (0, 2)}[input()] for _ in range(N)]
    ABC = [A, B, C]
    RR = ['A', 'B', 'C']
    R = []
    for (i, (s1, s2)) in enumerate(S):
        if ABC[s1] == 0 and ABC[s2] == 0:
            return (False, None)
        if ABC[s1] < ABC[s2]:
            (s1, s2) = (s2, s1)
        if A + B + C == 2 and ABC[s1] == 1 and (ABC[s2] == 1) and (i < N - 1) and (S[i] != S[i + 1]):
            (s1n, s2n) = S[i + 1]
            if s1 in [s1n, s2n]:
                (s1, s2) = (s2, s1)
        ABC[s1] -= 1
        ABC[s2] += 1
        R.append(RR[s2])
    return (True, R)


(a, s) = main()
if not a:
    print('No')
else:
    print('Yes')
    print('\n'.join(s))
