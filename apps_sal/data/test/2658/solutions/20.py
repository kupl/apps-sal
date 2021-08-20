(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [i - 1 for i in a]
d = [1] * n
p = 0
b = []
while d[p]:
    b.append(p)
    d[p] = 0
    p = a[p]
avant = b.index(p)
loop_count = len(b) - avant
c = b[avant:]
if k <= avant:
    print(b[k] + 1)
else:
    k -= avant
    k %= loop_count
    print(c[k] + 1)
