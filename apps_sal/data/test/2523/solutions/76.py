import itertools
S = list(itertools.accumulate([0] + [int(_) for _ in input()]))
N = len(S) - 1
for i in range(N, 0, -1):
    if 2 * i < N:
        break
    if S[i] - S[N - i] in [0, 2 * i - N]:
        break
print(i)
