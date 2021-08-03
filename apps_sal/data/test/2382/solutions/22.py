# https://atcoder.jp/contests/abc140/submissions/7397810

import sys

stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


n = ni()
a = na()
a.sort(reverse=True)

done = [False] * (1 << n)
b = [a[0]]
done[0] = True
for d in range(n):  # d: d-th trial is passed.
    j = 0  # j: skip num (already-generated or impossible-to-generate)
    for i in range(1 << d):  # Try split of i-th slim.
        while j < 1 << n and (done[j] or b[i] <= a[j]):
            j += 1
        if j == 1 << n:
            print("No")
            return
        b.append(a[j])  # b[i] > a[j]
        done[j] = True
    b.sort(reverse=True)
print("Yes")
