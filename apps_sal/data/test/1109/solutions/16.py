
n, k = map(int, input().split())
a = list(map(int, input().split()))

m = 0
for i in range(k):
    s = a[i::k]
    c = [s.count(x) for x in set(s)]
    m += len(s) - max(c)
print(m)
