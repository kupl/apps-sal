import sys
readline = sys.stdin.readline
T = int(readline())
Ans = [None] * T
for qu in range(T):
    (h1, w1, h2, w2) = map(int, readline().split())
    Ans[qu] = 1 + (w2 - w1) * (h2 - h1)
print('\n'.join(map(str, Ans)))
