import sys


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


S = sr()
K = ir()
cand = set()
length = len(S)
for i in range(length):
    for j in range(1, 6):
        cand.add(S[i:i + j])

answer = sorted(list(cand))[K - 1]
print(answer)
