import sys


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, M = lr()
S = sr()
# マスNからスタート
cur = N
answer = []
while cur > 0:
    for x in range(M, 0, -1):
        if cur - x < 0 or S[cur - x] == '1':
            continue
        answer.append(x)
        cur -= x
        break
    else:
        print((-1))
        return

answer = answer[::-1]
print((*answer))
# 53
