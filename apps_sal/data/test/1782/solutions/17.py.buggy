import sys

n, k = list(map(int, input().split()))

if k * 3 > n:
    print(-1)
    return


ans = [1] * n
if n == k * 3 and n % 2 == 1:
    if n == 3:
        print(-1)
        return
    l = n - (n % 6) - 6
    l = max(0, l)

    filled = 0
    f, s = 1, 2
    for i in range(l):
        if f > k:
            f = 1
        if s > k:
            s = 1
        if filled == k:
            break
        j = i % 6
        r = [f, f, s, f, s, s][j]
        ans[i] = r
        if j == 5:
            f, s = f + 2, s + 2
            filled += 1
        if j == 3:
            filled += 1
    tail = [k - 2, k - 2, k, k - 2, k - 1, k - 1, k, k, k - 1]
    for i in range(9):
        ans[l + i] = tail[i]
else:
    filled = 0
    f, s = 1, 2
    for i in range(n):
        if f > k:
            f = 1
        if s > k:
            s = 1
        if filled == k:
            break
        j = i % 6
        r = [f, f, s, f, s, s][j]
        ans[i] = r
        if j == 5:
            f, s = f + 2, s + 2
            filled += 1
        if j == 3:
            filled += 1

s = ' '.join(map(str, ans))
sys.stdout.write(s)
