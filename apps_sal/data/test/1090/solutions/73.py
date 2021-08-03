N, K = list(map(int, input().split(' ')))
S = input()

groups = 1
for s0, s1 in zip(S, S[1:]):
    if s0 != s1:
        groups += 1

groups = max(1, groups - 2 * K)

print((N - groups))
