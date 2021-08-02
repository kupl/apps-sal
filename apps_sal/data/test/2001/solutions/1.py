import sys
mod = 10**9 + 7
n, q = list(map(int, sys.stdin.readline().split()))
S = sys.stdin.readline().strip()
LR = [list(map(int, sys.stdin.readline().split())) for i in range(q)]

LIST = [0]
for s in S:
    if s == "1":
        LIST.append(LIST[-1] + 1)
    else:
        LIST.append(LIST[-1])


def count(m, n, mod):
    return (pow(2, m, mod) - 1) * pow(2, n, mod) % mod


for l, r in LR:
    print(count(LIST[r] - LIST[l - 1], r - l + 1 - LIST[r] + LIST[l - 1], mod))
