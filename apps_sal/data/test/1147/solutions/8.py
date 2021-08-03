from bisect import bisect_left
def R(): return list(map(int, input().split()))


n, x, k = R()
a = sorted(R())
cnt = 0
for u in a:
    l = ((u + x - 1) // x + k - 1) * x
    cnt += bisect_left(a, l + x) - bisect_left(a, max(u, l))
print(cnt)
