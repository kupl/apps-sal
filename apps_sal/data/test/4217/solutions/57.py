(n, m) = list(map(int, input().split()))
l = [0] * m
for i in range(n):
    (k, *a) = list(map(int, input().split()))
    for j in range(k):
        l[a[j] - 1] += 1
print(l.count(n))
