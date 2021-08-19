n = int(input())
a = list(map(int, input().split()))
asum = sum(a)
for i in range(1, n):
    if a[i] < a[i - 1]:
        a[i] = a[i - 1]
print(sum(a) - asum)
