(k, n) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
for i in range(n - 1):
    b.append(a[i + 1] - a[i])
b.append(a[0] + (k - a[-1]))
print(sum(b) - max(b))
