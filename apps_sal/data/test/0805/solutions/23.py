n = int(input())
a = [1] * 100
(x, y) = map(int, input().split())
for i in range(n - 1):
    (l, r) = map(int, input().split())
    for j in range(l, r):
        a[j] = 0
print(sum(a[x:y]))
