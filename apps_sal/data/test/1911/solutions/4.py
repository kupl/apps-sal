(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
c = a[-1] - a[0]
d = [a[i] - a[i - 1] for i in range(1, n)]
d = sorted(d)[::-1]
c -= sum(d[:k - 1])
print(c)
