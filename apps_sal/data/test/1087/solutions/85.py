import numpy as np


def binstr(n):
    return np.array(list(map(int, list(bin(n)[2:].rjust(40, '0')))))


(N, K) = map(int, input().split())
A = list(map(int, input().split()))
AA = sum([binstr(i) for i in A])
X = 0
ans = 0
for i in range(40):
    if AA[i] > N - AA[i]:
        ans += AA[i] * 2 ** (39 - i)
    elif X + 2 ** (39 - i) <= K:
        ans += (N - AA[i]) * 2 ** (39 - i)
        X += 2 ** (39 - i)
    else:
        ans += AA[i] * 2 ** (39 - i)
print(ans)
