import sys
from itertools import combinations
read = sys.stdin.read
(N, K, *xy) = map(int, read().split())
xy = sorted(zip(*[iter(xy)] * 2))
(X, Y) = zip(*xy)
answer = 10 ** 20
for (left, right) in combinations(range(N), 2):
    width = X[right] - X[left]
    tmp_Y = sorted(Y[left:right + 1])
    h = len(tmp_Y)
    for i in range(h):
        if i + K > h:
            break
        S = width * (tmp_Y[i + K - 1] - tmp_Y[i])
        if S < answer:
            answer = S
print(answer)
