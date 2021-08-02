import math
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

s = sum(A)


def yakusu(n):
    ans_local = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans_local = ans_local | set([i, n // i])  # setなので平方数でもOK
    return list(ans_local)  # 必要に応じてsort


yaku = sorted(yakusu(s), reverse=1)
# print(yaku)
for mod in yaku:
    B = [i % mod for i in A if i % mod != 0]
    if B == []: print(mod); return
    if len(B) == 1:
        q = B[0]
        if 0 <= q <= k or mod - k <= q: print(mod); return
        else: continue
    B.sort()
    r = [B[0]] * len(B)
    for i in range(len(B) - 1):
        r[i + 1] = r[i] + B[i + 1]
    now = float("INF")
    for i in range(1, len(B)):  # 切り方
        if r[i - 1] == mod * (len(B) - i) - (r[-1] - r[i - 1]) and r[i - 1] <= k:
            print(mod); return
