import math
import itertools


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


(N, X, Y) = list(map(int, input().split()))
L = [i for i in range(1, N + 1)]
c_list = list(itertools.combinations(L, 2))
Answer = {}
for i in range(1, N):
    inti = str(i)
    Answer[inti] = 0


def des(a, b):
    if b <= X or a >= Y:
        return b - a
    else:
        return min(b - a, abs(Y - b) + abs(X - a) + 1)


for cl in c_list:
    a = cl[0]
    b = cl[1]
    inti = des(a, b)
    inti = str(inti)
    Answer[inti] += 1
for (n, m) in list(Answer.items()):
    print(m)
