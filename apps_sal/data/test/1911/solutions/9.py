(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n - 1):
    b.append(a[i + 1] - a[i])
b.sort()
print(sum(b[:len(b) - k + 1]))
