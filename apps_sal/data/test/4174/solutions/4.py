import bisect
(n, x) = map(int, input().split())
l = [0] + list(map(int, input().split()))
for i in range(n):
    l[i + 1] += l[i]
print(bisect.bisect_left(l, x + 1))
