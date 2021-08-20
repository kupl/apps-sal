from bisect import bisect_left
(n, k) = list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort()
i = bisect_left(h, k)
print(n - i)
