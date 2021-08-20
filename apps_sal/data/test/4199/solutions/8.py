(n, k) = map(int, input().split())
h = list(map(int, input().split()))
c = 0
for e in h:
    if e >= k:
        c += 1
print(c)
