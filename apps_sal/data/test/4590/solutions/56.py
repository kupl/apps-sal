from itertools import accumulate as a
(N, M, K) = map(int, input().split())
l = [0]
P = l + list(a(map(int, input().split())))
Q = l + list(a(map(int, input().split())))
i = j = 0


def f():
    return P[i] + Q[j] <= K


while i <= N and f():
    i += 1
while i >= 0:
    i -= 1
    while j <= M and f():
        j += 1
    l += [i + j - 1]
print(max(l))
