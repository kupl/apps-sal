n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n - 2, -1, -1):
    a[i] = max(min(a[i], a[i + 1] - 1), 0)
print(sum(a))

