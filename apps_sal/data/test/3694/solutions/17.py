from collections import Counter
import sys
readline = sys.stdin.readline


def check(A):
    CA = Counter(A)
    if CA[0] >= 2:
        return False
    cnt = 0
    for (k, v) in list(CA.items()):
        if v > 2:
            return False
        if v == 2 and CA[k - 1] >= 1:
            return False
        if v >= 2:
            cnt += 1
    if cnt >= 2:
        return False
    L = len(A)
    if (sum(A) - L * (L - 1) // 2) % 2 == 0:
        return False
    return True


N = int(readline())
if check(list(map(int, readline().split()))):
    print('sjfnb')
else:
    print('cslnb')
