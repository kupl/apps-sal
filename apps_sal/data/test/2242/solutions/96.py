from itertools import accumulate

S = input()

R = [1]
for _ in range(len(S) - 1):
    R.append(R[-1] * 10 % 2019)

L = [int(s) * r for s, r in zip(reversed(S), R)]
Z = list(accumulate(L, func=lambda a, b: (a + b) % 2019))

T = [1] + [0] * 2018
for z in Z:
    T[z] += 1

f = lambda n: n * (n - 1) // 2
print(sum(f(t) for t in T))
