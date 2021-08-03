def q(): return map(int, input().split())


n, k = q()
a = []
while(n):
    a += [q()]
    n -= 1
print((k - sum(r - l + 1 for l, r in a) % k) % k)
