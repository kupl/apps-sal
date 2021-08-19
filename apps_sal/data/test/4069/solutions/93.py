import sys
readline = sys.stdin.readline
(X, K, D) = map(int, readline().split())
X = abs(X)
if X - K * D > 0:
    print(X - K * D)
else:
    cnt = X // D
    point = X % D
    if (K - cnt) % 2 == 1:
        print(abs(point - D))
    else:
        print(point)
