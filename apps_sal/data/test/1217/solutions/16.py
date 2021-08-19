import bisect
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
c = [bisect.bisect_right(a, i) for i in b]
print(' '.join(map(str, c)))
