# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K, C = lr()
S = sr()
# 左からと右からでそれぞれ貪欲、重なったところが必須
left = []; right = []

def work(S):
    ret = []
    cur = 0
    count = 0
    while count < K:
        if S[cur] == 'o':
            count += 1
            ret.append(cur)
            cur += C + 1
        else:
            cur += 1
    return ret

left = work(S)
right = work(S[::-1])
right = [N-1-x for x in right]
right.reverse()
answer = []
for l, r in zip(left, right):
    if l == r:
        answer.append(str(l+1))
print(('\n'.join(answer)))

