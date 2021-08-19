import sys
from collections import Counter


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


H, W, N = lr()
pairs = []
for _ in range(N):
    a, b = lr()
    a -= 1
    b -= 1
    for dh in [-2, -1, 0]:
        if a + dh < 0 or a + dh > H - 3:
            continue
        for dw in [-2, -1, 0]:
            if b + dw < 0 or b + dw > W - 3:
                continue
            pairs.append((a + dh, b + dw))

counter = Counter(pairs)
answer = [0] * 10
counter2 = Counter(list(counter.values()))
for k, v in list(counter2.items()):
    answer[k] = v

answer[0] = (H - 2) * (W - 2) - sum(answer)
print(('\n'.join(map(str, answer))))
# 30
