globCnt = 0


def rec(root):
    nonlocal globCnt, cnt
    if root - 1 >= len(cnt):
        return 0
    l = rec(2 * root + 1)
    r = rec(2 * root + 2)
    if l != r:
        globCnt += abs(l - r)
    return max(l, r) + cnt[root - 1]


n = int(input())
cnt = list(map(int, input().split()))

rec(0)
print(globCnt)
