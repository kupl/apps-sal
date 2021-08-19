from bisect import bisect_left
(n, *l) = list(map(int, open(0).read().split()))
l.sort()
print(sum((bisect_left(l, l[i] + l[j]) - 1 - j for i in range(n) for j in range(i + 1, n))))
