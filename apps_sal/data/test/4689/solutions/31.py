k, n = map(int, input().split())

a = list(map(int, input().split()))

a.append(a[0] + k)

m = 0

for i in range(n):
    m = max(m, a[i + 1] - a[i])

print(k - m)
