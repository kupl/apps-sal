n, m = map(int, input().split())
l = [0] * m
for i in range(n):
    a = list(map(int, input().split()))
    del a[0]
    for i in a:
        l[i - 1] += 1
print(l.count(n))
