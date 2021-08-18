
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

d = [0] * (n + 1)

for i in range(n):
    d[a[i]] += 1

d.sort()

print((sum(d[:n - k + 1])))
