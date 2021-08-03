import numpy as np

N = int(input())
S = np.array(list(input()))


def match_length(s1, s2, m):
    x = np.zeros(len(s1) + 2, dtype=bool)
    x[1:-1] = (s1 == s2)

    l = max(np.diff(np.nonzero(x == 0)[0]) - 1)
    return min(m, l)


ans = 0
for i in range(1, N - 1):
    ans = max(ans, match_length(S[i:], S[:-i], i))
print(ans)
