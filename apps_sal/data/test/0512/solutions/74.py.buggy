import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())


sys.setrecursionlimit(10**9)

N = int(input())

As = set()
Bs = set()
dirc = [0] * (N * 2)
pair = [-1] * (N * 2)
for _ in range(N):
    a, b = mapint()
    if a != -1 and b != -1:
        if dirc[a - 1] != 0 or dirc[b - 1] != 0 or b <= a:
            print('No')
            return
        dirc[a - 1] = 1
        pair[a - 1] = b - 1
        dirc[b - 1] = -1
        pair[b - 1] = a - 1
    elif a != -1:
        if dirc[a - 1] != 0:
            print('No')
            return
        As.add(a - 1)
        dirc[a - 1] = 1
    elif b != -1:
        if dirc[b - 1] != 0:
            print('No')
            return
        Bs.add(b - 1)
        dirc[b - 1] = -1

dp = [0] * (N * 2 + 1)
dp[0] = 1
for l in range(1, N * 2):
    if not dp[l - 1]:
        continue
    for r in range(l + 1, N * 2 + 1):
        if (r - l + 1) % 2 != 0:
            continue
        _range = (r - l + 1) // 2
        tmp = [0] * (N * 2 + 1)
        for i in range(l - 1, r):
            d = dirc[i]
            if d == 0:
                continue
            p = pair[i]
            if (d == -1 and i - _range < l - 1) or (d == 1 and i + _range >= r):
                break
            if p >= r or (p != -1 and p < l - 1):
                break
            tmp[i] = 1
            if p == -1:
                if d == 1:
                    if i + _range >= r or i + _range in Bs:
                        break
                    tmp[i + _range] = 1
                elif d == -1:
                    if i - _range < l - 1 or i - _range in As:
                        break
                    tmp[i - _range] = 1
                else:
                    pair_idx = i + _range if i + _range < r else i - _range
                    tmp[pair_idx] = 1
            else:
                if abs(p - i) != _range or (tmp[p] != 0 and pair[p] != i):
                    break
                tmp[p] = 1
        else:
            dp[r] = 1
print('Yes' if dp[-1] else 'No')
