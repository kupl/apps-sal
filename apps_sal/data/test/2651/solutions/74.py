import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
X = list(map(int, readline().split()))
Y = list(map(int, readline().split()))
DIV = 10 ** 9 + 7


xsum = 0
for i in range(1, len(X)):
    edge = X[i] - X[i - 1]
    times = i * (N - i)
    xsum += ((edge % DIV) * (times % DIV)) % DIV
    xsum %= DIV

ysum = 0
for i in range(1, len(Y)):
    edge = Y[i] - Y[i - 1]
    times = i * (M - i)
    ysum += ((edge % DIV) * (times % DIV)) % DIV
    ysum %= DIV

print((xsum * ysum) % DIV)
