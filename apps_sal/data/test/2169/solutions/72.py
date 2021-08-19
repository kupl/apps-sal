import sys
input = sys.stdin.readline
(h, w, d) = list(map(int, input().split()))
n = h * w
a = [0] * n
for i in range(h):
    t = list(map(int, input().split()))
    for j in range(w):
        a[w * i + j] = t[j] - 1


def dist(i, j):
    dh = abs(i // w - j // w)
    dw = abs(i % w - j % w)
    return dh + dw


idx_list = [0] * n
for i in range(n):
    idx_list[a[i]] = i
dist_list = [0] * n
for i in range(n):
    if i < d:
        dist_list[i] = 0
    else:
        dist_list[i] = dist_list[i - d] + dist(idx_list[i - d], idx_list[i])
q = int(input())
for i in range(q):
    (l, r) = list(map(int, input().split()))
    l -= 1
    r -= 1
    print(dist_list[r] - dist_list[l])
