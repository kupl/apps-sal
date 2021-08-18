import sys


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


"""
全体からあまりがK未満を引く
"""
N, K = lr()
total = N * N
for b in range(1, N + 1):
    if b <= K:
        total -= N
    else:
        total -= K * (N // b) + max(0, min(N % b, K - 1))

answer = total
print(answer)
