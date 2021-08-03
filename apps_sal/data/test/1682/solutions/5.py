from bisect import bisect

n, k = list(map(int, input().split()))

aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

dd = sorted(a - b for a, b in zip(aa, bb))
k = max(k, bisect(dd, 0))

print(sum(bb) + sum(dd[:k]))
