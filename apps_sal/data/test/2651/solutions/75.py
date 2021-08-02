import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
X = list(map(int, readline().split()))
Y = list(map(int, readline().split()))
DIV = 10 ** 9 + 7


def f(V):
    vsum = 0
    for i in range(1, len(V)):
        vsum += (((V[i] - V[i - 1]) % DIV) * ((i * (len(V) - i)) % DIV)) % DIV
        vsum %= DIV
    return vsum


print((f(X) * f(Y)) % DIV)
