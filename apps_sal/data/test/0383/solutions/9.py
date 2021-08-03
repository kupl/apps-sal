n, k, d = map(int, input().split())
a = [1]
b = [0]
for i in range(1, n + 1):
    a.append(sum(a[max(i - d + 1, 0):]))
    b.append(sum(a[max(i - k, 0):max(i - d + 1, 0)]) + sum(b[max(i - k, 0):]))
print(b[n] % (10**9 + 7))
