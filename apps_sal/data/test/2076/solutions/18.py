import sys
readline = sys.stdin.readline

N = int(readline())

Ans = [None] * N
for qu in range(N):
    A, B, C = map(int, readline().split())
    res = 0
    for a in range(A + 1):
        if 2 * a > B:
            break
        cnt = 3 * a
        t = B - 2 * a
        t = min(t, C // 2)
        cnt += 3 * t
        res = max(res, cnt)
    Ans[qu] = res

print('\n'.join(map(str, Ans)))
