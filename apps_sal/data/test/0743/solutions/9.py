n = int(input())
a = list(map(int, input().split()))
for i in range(n * 2):
    a = sorted(a, reverse=True)
    for j in range(1, n):
        while a[j] and a[0] > a[j]:
            a[0] -= a[j]
print(sum(a))
