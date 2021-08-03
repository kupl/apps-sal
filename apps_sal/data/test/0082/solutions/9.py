n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = sum(a)
p = (k - 0.5) * n
if s >= p:
    print(0)
else:
    r = int(2 * (p - s))
    print(r)
