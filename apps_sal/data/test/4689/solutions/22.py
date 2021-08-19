(k, n) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
for i in range(n - 1):
    b.append(a[i + 1] - a[i])
b.append(k - a[-1] + a[0])
print(sum(b) - max(b))
